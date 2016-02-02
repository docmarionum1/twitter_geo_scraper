from auth import getTwitter
from setup import setup

import time
import datetime
import csv
import json
import sqlite3
import signal
import sys
import os

# create DB if does not exist
if not os.path.isfile(os.getenv('PWD') + '/twitter.db'):
    print 'creating DB'
    setup()


# Connect to DB
conn = sqlite3.connect('twitter.db')

def signal_handler(signal, frame):
    # Close connection on interrupt
    conn.close()
    sys.stdout.flush()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

twitter = getTwitter()

nodes = [
    #{'geocode': '40.783288,-73.967090,7mi', 'since': '0'},
    #{'geocode': '40.729992,-73.993841,7mi', 'since': '0'},
    #{'geocode': '40.830778,-73.942806,7mi', 'since': '0'}
    {'geocode': '40.830956,-73.910179,7mi', 'since': '0'},
    {'geocode': '40.663972,-73.956871,8mi', 'since': '0'},
    {'geocode': '40.688708,-73.779544,8mi', 'since': '0'},
    {'geocode': '40.580584,-74.152908,9mi', 'since': '0'}
]

# Total of 20 seconds sleep between rounds
sleep = 20.

while True:
    for node in nodes:
        # Execute Query
        try:
            t = twitter.search.tweets(geocode=node['geocode'], result_type='recent',
                count=100, since_id=node['since'])
        except Exception, e:
            print e
            # Could be twitter is overloaded, sleep for a minute before starting again
            time.sleep(60)
            continue

        # Update since 
       # node['since'] = t['search_metadata']['max_id_str']

        # Print status
        print node['geocode'], len(t['statuses']), str(datetime.datetime.now())

        # Go through the results and create arrays to add to DB
        tweets = []
        users = []

        for status in t['statuses']:
            user = status['user']
            del status['user']
            timestamp = datetime.datetime.strptime(
                status['created_at'], 
                '%a %b %d %H:%M:%S +0000 %Y'
            )

            tweets.append((
                status['id'], 
                status['text'], 
                json.dumps(status['geo']),
                timestamp,
                user['id'],
                json.dumps(status)
            ))
            users.append((
                user['id'],
                timestamp,
                json.dumps(user)
            ))

        # Add to DB
        try:
            cursor = conn.cursor()
            cursor.executemany('INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?)', tweets)
            cursor.executemany('INSERT OR IGNORE INTO users VALUES (?, ?, ?)', users)
            conn.commit()

            node['since'] = t['search_metadata']['max_id_str']
        except:
            time.sleep(60)
            conn = sqlite3.connect('twitter.db')

        # Sleep between nodes
        time.sleep(sleep/len(nodes))

    sys.stdout.flush()
