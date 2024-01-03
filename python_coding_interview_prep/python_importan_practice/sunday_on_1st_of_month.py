"""
Sunday on the 1st of a month

A leap year is an year in which month of feb is 29 days. If it is divisble by 4.
But also divisible by 100 then it is not a leap year.
april, june, september and november is 30 days
january, march, may, july, august, october and december is 31 days.
1st jan 1900 was monday.
write a program to find out how many sundays fell of the first of the month 
for a given year which is >= 1900. 

"""
import calendar


cal= calendar.TextCalendar(calendar.SUNDAY)
print(cal.prmonth(2019,1)
print(calendar.SUNDAY)