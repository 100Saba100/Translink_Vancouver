import requests

API_KEY = "tqpeEfR5dRWGpXX3VLhL"
url = f"https://gtfsapi.translink.ca/v3/gtfsrealtime?apikey={API_KEY}"

response = requests.get(url)

if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    exit()

# The feed is in Protocol Buffers (GTFS-RT), not JSON.
# We'll need the `gtfs-realtime-bindings` library to parse it.
from google.transit import gtfs_realtime_pb2
print("GTFS-Realtime bindings imported successfully!")

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)

# Print out some basic info
#for entity in feed.entity:
    # if entity.HasField('trip_update'):
    #     trip = entity.trip_update
        # for stop_time in trip.stop_time_update:
        #     print("Stop ID:", stop_time.stop_id)
        #     if stop_time.HasField('arrival'):
        #         print("  Arrival time (epoch):", stop_time.arrival.time)
    #     print(trip)

target_stop = "4195"
# t_stop = "4215"
# des_stop = "10866"
for entity in feed.entity:
    if entity.HasField("trip_update"):
    #     print("=== Trip Update ===")
    #     print(entity.trip_update)

    # if entity.HasField("vehicle"):
    #     print("=== Vehicle Position ===")
    #     print(entity.vehicle)

    # if entity.HasField("alert"):
    #     print("=== Alert ===")
    #     print(entity.alert)
        # print("trip ID: ", entity.id)
        trip = entity.trip_update
        for stu in trip.stop_time_update:
            if stu.stop_id == target_stop:
                print("trip ID: ", entity.id)
                print("Found update for stop:", target_stop)
                print("Sequence:", stu.stop_sequence)
                
                # These fields may or may not exist
                if stu.HasField("arrival"):
                    print("Arrival delay:", stu.arrival.delay)
                if stu.HasField("departure"):
                    print("Departure delay:", stu.departure.delay)

                print("Schedule relationship:", stu.schedule_relationship)