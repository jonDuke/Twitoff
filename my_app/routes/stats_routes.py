# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from datetime import datetime

from my_app.models import db, User, Tweet, Search
from my_app.services.basilica_service import basilica_api_client

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")
    # todo: wrap in a try block in case the user's don't exist in the database
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    print("-----------------")
    print("TRAINING THE MODEL...")
    embeddings = []
    labels = []
    for tweet in user_a_tweets:
        labels.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)

    #classifier = LogisticRegression()
    classifier = DecisionTreeClassifier()
    classifier.fit(embeddings, labels)

    print("-----------------")
    print("MAKING A PREDICTION...")

    basilica_api = basilica_api_client()
    example_embedding = basilica_api.embed_sentence(tweet_text)
    result = classifier.predict([example_embedding])

    # save search to db
    new_search = Search()
    new_search.user_a = screen_name_a
    new_search.user_b = screen_name_b
    new_search.tweet = tweet_text
    new_search.prediction = result[0]
    new_search.timestamp = datetime.now()
    db.session.add(new_search)
    db.session.commit()
    
    return render_template("twitoff_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely= result[0]
    )
