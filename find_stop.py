import sqlite3
import re
#import os

def get_stop_name():
    while True:
        st = input("From Where?\t").strip()
        
        #check input
        if len(st)==0 or len(st) >30:
            print("input not valid\n try again!")
            continue
        if not re.match(r"^[\w\s\-\']+$", st):
            print("Stop name contains invalid characters")
            continue
        return st

def find_stop_id():
    stop = get_stop_name()        
    search_pattern = f"%{stop}%"

    conn = sqlite3.connect("gtfs_s.db")
    cursor = conn.cursor()


    cursor.execute(
        ''' SELECT stop_id, stop_name
        FROM stops
        WHERE stop_name LIKE ? COLLATE NOCASE''', (search_pattern,)
    )

    results = cursor.fetchall()
    print(results)

    # for stop_id, stop_name in results:
    #     print(stop_id, stop_name)

    conn.close()

    #user choose from options
    for i, (stop_id, stop_name) in enumerate(results, start = 1):
        print(f"{i}) {stop_name} ({stop_id})")
    user_choice = input("Select an Option or (q) to quit:\t").strip().lower()
    # print(f"i:\t{i}")
    if user_choice == "q":
        exit()
    if user_choice.isdigit() and int(user_choice) <= i:
        # print(results[int(user_choice)-1])
        # print(results[int(user_choice)-1][0])
        return results[int(user_choice)-1][0]
