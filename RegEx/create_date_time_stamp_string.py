import re
import datetime

time_stamp = re.sub('[^A-Za-z0-9]+','',str(datetime.datetime.now()))
print(times_stamp)
