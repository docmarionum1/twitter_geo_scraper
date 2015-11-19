import sqlite3
import csv
from unicodeCSV import UnicodeWriter
import json

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

with open('users.csv', 'wb') as f:
    #csvwriter = csv.writer(f)
    csvwriter = UnicodeWriter(f)
    csvwriter.writerow(['userid', 'timestamp', 'raw'])
    for row in c.execute('SELECT id, timestamp, raw from users where timestamp >= "2015-11-04 22:00:00" and timestamp < "2015-11-04 23:00:00"'):
        csvwriter.writerow([row[0], row[1], row[2]])
