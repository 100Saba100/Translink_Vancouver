import sqlite3
import os

stop = input("From Where?\t").strip()

conn = sqlite3.connect("gtfs_s.db")
cursor = conn.cursor()

cursor.execute(
    f''' SELECT stop_id, stop_name
    FROM stops
    WHERE stop_name LIKE "%{stop}%"
'''
)


