import sqlite3
import os

stop = input("From Where?\t").strip()
search_pattern = f"%{stop}%"

conn = sqlite3.connect("gtfs_s.db")
cursor = conn.cursor()


cursor.execute(
    ''' SELECT stop_id, stop_name
    FROM stops
    WHERE stop_name LIKE ? COLLATE NOCASE''', (search_pattern,)
)

results = cursor.fetchall()

# for stop_id, stop_name in results:
#     print(stop_id, stop_name)

conn.close()

#user choose from options
for i, (stop_id, stop_name) in enumerate(results, start = 1):
    print(f"{i}) {stop_name} ({stop_id})")
user_choice = input("Select an Option or (q) to quit:\t").strip().lower()
if user_choice == "q":
    exit()
if user_choice.isdigit():
    print(results[int(user_choice)-1])
