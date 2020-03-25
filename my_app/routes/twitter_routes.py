# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify

from my_app.models import db, Tweet, User, parse_records
from my_app.services.twitter_service import twitter_api_client
from my_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

def store_twitter_data(screen_name):
    """ stores twitter data for the given user in the database """
    # get twitter info
    api = twitter_api_client()
    twitter_user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, 
                                 exclude_replies=False, include_rts=False)

    # save or update user object
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # convert tweet text into embeddings with Basilica
    #print("STATUS COUNT:", len(statuses))
    basilica_api = basilica_api_client()
    all_tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_api.embed_sentences(all_tweet_texts, 
                                                   model="twitter"))
    #print("NUMBER OF EMBEDDINGS", len(embeddings))

    # save or update tweet objects
    counter = 0
    for status in statuses:
        #print(status.full_text)
        #print("----")
        #print(dir(status))

        # Find or create database tweet:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embeddings[counter]
        db.session.add(db_tweet)
        counter+=1

    db.session.commit()    
    print(f"Added user {db_user.name} with {len(statuses)} tweets")

    return db_user, statuses

@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    db_users = User.query.all()
    users_response = parse_records(db_users)
    return jsonify(users_response)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    #print(screen_name)
    db_user, statuses = store_twitter_data(screen_name)
    #return "OK"
    return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets
