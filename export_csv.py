import sqlite3
import csv
from unicodeCSV import UnicodeWriter
import json

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

with open('tweets.csv', 'wb') as f:
    #csvwriter = csv.writer(f)
    csvwriter = UnicodeWriter(f)
    csvwriter.writerow(['tweetid', 'timestamp', 'latitude', 'longitude', 'tweet', 'userid', 'raw'])
    #for row in c.execute('SELECT geo, tweet, timestamp, user_id from tweets WHERE geo != "null"'):
    for row in c.execute('SELECT id, timestamp, geo, tweet, user_id, raw from tweets WHERE geo != "null" and timestamp >= "2015-11-04 22:00:00" and timestamp < "2015-11-04 23:00:00"'):
        geo = json.loads(row[2])
        lat = geo['coordinates'][0]
        lon = geo['coordinates'][1]
        csvwriter.writerow([row[0], row[1], lat, lon, row[3], row[4], row[5]])
