# SQL mit Python
import sqlite3

# connects to a DB, if it doesn't exists, first it will create it
conn = sqlite3.connect("test.db")








# close connection
conn.close()