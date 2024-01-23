# Context:
# This script calculates the time difference in seconds between two timestamps provided as input.
# It uses the datetime module to parse timestamps and calculate the absolute time difference.

# Importing the datetime module for handling timestamps.
import datetime

# Taking the number of test cases as input.
cas = int(input())

# Specifying the format of the timestamp.
time_format = "%a %d %b %Y %H:%M:%S %z"

# Looping through each test case.
for _ in range(cas):
    # Taking two timestamps as input.
    timestamp1 = input().strip()
    timestamp2 = input().strip()

    # Converting timestamps to datetime objects.
    time_second1 = datetime.datetime.strptime(timestamp1, time_format)
    time_second2 = datetime.datetime.strptime(timestamp2, time_format)

    # Calculating and printing the absolute time difference in seconds.
    print(int(abs((time_second1 - time_second2).total_seconds())))
