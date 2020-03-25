# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()


class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)
    # comments = db.Column(db.Integer)
    # likes = db.Column(db.Integer)
    # retweets = db.Column(db.Integer)
    # timestamp = db.Column(db.DateTime)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String(128))
    name = db.Column(db.String(128))
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    tweet_count = db.Column(db.Integer)
    tweets = db.relationship('Tweet', backref='users')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
