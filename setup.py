import sqlite3

def setup():
	conn = sqlite3.connect('twitter.db')

	c = conn.cursor()

	c.execute('''CREATE TABLE tweets (id INTEGER PRIMARY KEY, tweet TEXT, geo TEXT, timestamp TEXT, user_id INTEGER, raw TEXT)''')
	c.execute('''CREATE TABLE users (id INTEGER, timestamp TEXT, raw TEXT, CONSTRAINT pk PRIMARY KEY (id, timestamp))''')

	conn.commit()
	conn.close()


if __name__ == '__main__':
	setup()