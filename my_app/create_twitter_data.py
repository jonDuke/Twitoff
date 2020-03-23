# create_twitter_data.py

# inserts some placeholder tweet and user data into the database
from datetime import date
import random
import string

# set up the sqlite3 connection
import sqlite3
conn = sqlite3.connect('my_app/my_app_12.db')
cursor = conn.cursor()

# enter some users
query = """
INSERT INTO users (name, handle, followers)
VALUES ("John Smith", "@jsmith", 10),
    ("Sarah Connor", "@sconnor", 35),
    ("Pink Panther", "@ppanther", 50),
    ("Pikachu", "@pikapi", 1536),
    ("A pine tree", "@randomtree", 3);
"""
cursor.execute(query)

# enter some tweets (with random info for fun)
query = """
INSERT INTO tweets (author_id, text, comments, likes, retweets, timestamp)
VALUES"""
# generating random dates from this year (Jan 1st to today)
start_dt = date.today().replace(day=1, month=1).toordinal()
end_dt = date.today().toordinal()
for _ in range(20):  # creates this many tweets
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    random_text = "".join([random.choice(string.ascii_lowercase) for i in range(20)])
    #            author_id              text           comments                likes                   retweets                timestamp
    query += f'\n({random.randint(1,5)}, "{random_text}", {random.randint(0,20)}, {random.randint(0,50)}, {random.randint(0,10)}, "{random_day}"),'
query = query[:-1] + ';'  # remove the extra , and end with ;
cursor.execute(query)

# commit and close
conn.commit()
cursor.close()
conn.close()
