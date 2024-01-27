# Excercise

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime

from datetime import datetime

dt_object = datetime(2022, 1, 27, 12, 0, 0)  # Replace with your datetime
timestamp = dt_object.timestamp()

print("Datetime:", dt_object)
print("Timestamp:", timestamp)


# sleep using timestamp
import time

seconds_to_sleep = 5
print(f"Sleeping for {seconds_to_sleep} seconds...")
time.sleep(seconds_to_sleep)
print("Awake!")


# working with timezones

from datetime import datetime
import pytz

dt_object = datetime.now(pytz.timezone('US/Eastern'))
print("Current Time in US/Eastern:", dt_object)

