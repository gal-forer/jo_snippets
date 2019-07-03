import datetime
import pytz
import bubble_sort
# link to the page that it's taken from https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
# creates a datetime object with a costume date format
x = datetime.datetime.strptime("12/27/2010 15:38", "%m/%d/%Y %H:%M")
x2 = datetime.datetime.strptime("12/25/2010 17:38", "%m/%d/%Y %H:%M")
# print a date as a costume format
print x.strftime("%m/%d/%Y %H:%M")
# creates a new timezone object
timezone = pytz.timezone("UTC")
# sets the timezone to the datetime object
x = timezone.localize(x)
x2 = timezone.localize(x2)
# prints the time zone
# print x.tzinfo
# # converts the timezone
# x = x.astimezone(pytz.timezone("US/Eastern"))
# print x.strftime("%m/%d/%Y %H:%M")
# print x.tzinfo

'''
prints all the available timezones
'''
# for tz in pytz.all_timezones:
#     print tz
# sort the datetime objects
l = []
l.append(x)
l.append(x2)
print boobe_sort.bubblesort(l)