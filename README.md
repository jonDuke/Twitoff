# About Twitoff

Twitoff is a simple web app made as part of a class assignment. It was built in the Data Science course at Lambda School in March 2020, taught by professor Mike Rossetti.

Its primary function is to provide an interface to a machine learning model. The model takes two Twitter users and a made up tweet, and attempts to predict which of the users is more likely to post it.

The app currently uses a simple Decision Tree model, and learns from about 100-150 actual tweets from each user before it makes a prediction.

Visit the live app here! https://twitoff-jonduke.herokuapp.com

Note: the Twitter API access is currently broken, so the app is unable to add new Twitter users at this time.

### Technologies Used:

- Flask - a Python framework used to build the website itself
- SQL - production uses a PostGreSQL database to store persistent data
- Twitter API - the app pulls a collection of tweets for each user and stores them - for later use
- Basilica API - a machine learning API that converts the tweet text into embeddings that are useable by most machine learning models
- ScikitLearn - the actual prediction uses classification models from ScikitLearn
- Bootstrap 4 - for the CSS look and feel of the site, mostly configured by Prof. Rossetti
- Heroku - the app itself is hosted on Heroku
- GitHub - for source control

---

# Local Deployment Instructions

Clone the repo, then navigate there from the command-line:
```
cd Twitoff/
```

Create a file in the root directory named ".env", and fill in the required credentials.
```
# Environment variables
BASILICA_API_KEY="____"
TWITTER_API_KEY="____"
TWITTER_API_SECRET="____"
TWITTER_ACCESS_TOKEN="____"
TWITTER_ACCESS_TOKEN_SECRET="____"

# key needed for flash messaging.  Can be whatever, it just needs to exist.
FLASH_SECRET="whatever"

# credentials for admin functions
ADMIN_NAME="admin"
ADMIN_PASS="password"
```

Setup and activate the virtual environment, and install package dependencies:
```
pipenv install
pipenv shell
```

Setup the database (uses sqlite3 by default):
```
FLASK_APP=my_app flask db init
FLASK_APP=my_app flask db migrate
FLASK_APP=my_app flask db upgrade
```

Run the app:
```
FLASK_APP=my_app flask run
```

Then visit localhost:5000 in the browser to view the app!
