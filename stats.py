import sqlite3
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

print 'Tweets:', c.execute('SELECT COUNT(*) FROM tweets').fetchone()[0]
print 'Unique Users: ', c.execute('SELECT COUNT(distinct id) FROM users').fetchone()[0]

import os
print "DB Size:"
os.system('du -h twitter.db')
