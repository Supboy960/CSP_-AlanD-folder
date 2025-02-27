#AlAN dE lARA, HOw TO GET TIME OF DAY
import time

#frist instace of time in promgtinin
first_time = time.gmtime()
#print(first_time)

#Current time in seconds
current = time.time()
#print(current) #Seconds since jan 1 1970

#Current date and time like we see it naomally
now = time.ctime(current)
#print(now)

#Get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour #millitary time (0-23)
print(hour)
