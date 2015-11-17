#!/usr/bin/python
import time;  # This is required to include time module.
import calendar

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

# current time
localtime = time.localtime(time.time())
print "Local current time :", localtime

# format
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

# calendar
cal = calendar.month(2014, 11)
print "Here is the calendar:"
print cal;
