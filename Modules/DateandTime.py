import time
import datetime

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))


print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
