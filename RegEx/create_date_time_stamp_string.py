import re
import datetime


time_now = str(datetime.datetime.now())
print(time_now)

# remove all characters except numeric and alphabet
time_stamp = re.sub('[^A-Za-z0-9]+','',time_now)
print(time_stamp)
