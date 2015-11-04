from auth import getTwitter
import time
import datetime
import csv

twitter = getTwitter()
#query = 'geocode=40.7207038,-74.0065265,5min'
geocode = '40.783288,-73.967090,10mi'
#print [t['text'] for t in twitter.search.tweets(geocode=geocode)['statuses']]

with open('out.csv', 'wb') as f:
    writer = csv.writer(f)

    since = "0"
    while True:
        t = twitter.search.tweets(geocode=geocode, result_type='recent',
            count=100, since_id=since)

        since = t['search_metadata']['max_id_str']

        print len(t['statuses']), str(datetime.datetime.now())
        writer.writerow([len(t['statuses']), str(datetime.datetime.now())])
        f.flush()
        time.sleep(15)

