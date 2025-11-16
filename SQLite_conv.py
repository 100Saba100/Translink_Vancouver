import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("gtfs_s.db")
gtfs_static_dir = "/Users/saba/Translink_prj/gtfs_static"

for textfile in os.listdir(gtfs_static_dir):
    textfile_path = os.path.join(gtfs_static_dir, textfile)
    table_name = textfile.replace(".txt", "")
    
    # Load CSV into DataFrame
    df = pd.read_csv(textfile_path)

    # Write DataFrame into SQL table
    df.to_sql(table_name, conn, if_exists="replace", index=False)

# Optional: add indexes for speed (good practice)
indexes = [
    ("stops", "stop_id"),
    ("stop_times", "stop_id"),
    ("stop_times", "trip_id"),
    ("trips", "trip_id"),
    ("trips", "route_id"),
    ("routes", "route_id")
]

for table, column in indexes:
    try:
        conn.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{table}_{column} ON {table} ({column});"
        )
    except Exception as e:
        print(f"Index for {table}.{column} skipped: {e}")

# 5. Save everything
conn.commit()
conn.close()

print("GTFS Static imported successfully!")