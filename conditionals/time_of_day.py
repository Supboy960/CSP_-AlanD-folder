#Alan De Lara, Time of Day - Python

import time
first_time = time.gmtime()
current = time.time()
now = time.ctime(current)
local_time = time.localtime(current)
hour = local_time.tm_hour # millitary time (0-23)
print(hour)

if(hour <= 12):
    print("Good morning!")
elif(hour <= 17 and hour >= 12):
    print("Good afternoon!")
else:
    print("Good evening!")
