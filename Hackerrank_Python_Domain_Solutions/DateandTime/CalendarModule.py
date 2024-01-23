# Context:
# This script takes input in the form of month, day, and year, and then determines 
# the corresponding day of the week for that date.
# It utilizes the datetime and calendar modules to perform the required calculations.

# Importing necessary modules for handling date and calendar information.
import calendar
import datetime

# Taking input for month, day, and year.
m, d, y = map(int, input().split())

# Creating a datetime object with the input date.
input_date = datetime.date(y, m, d)

# Printing the uppercase name of the day corresponding to the input date.
print(calendar.day_name[input_date.weekday()].upper())

# get the week of the year for the input date
print(input_date.isocalendar()[1])
