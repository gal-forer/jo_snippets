import datetime
import pytz

# creates a datetime object with a costume date format
x = datetime.datetime.strptime("12/25/2010 10:38", "%m/%d/%Y %H:%M")
# print a date as a costume format
print x.strftime("%m/%d/%Y %H:%M")
# creates a new timezone object
timezone = pytz.timezone("UTC")
# sets the timezone to the datetime object
x = timezone.localize(x)
# prints the time zone
print x.tzinfo
# converts the timezone
x = x.astimezone(pytz.timezone("US/Eastern"))
print x.strftime("%m/%d/%Y %H:%M")
print x.tzinfo

'''
prints all the available timezones
'''
# for tz in pytz.all_timezones:
#     print tz