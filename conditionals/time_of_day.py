#Alan De Lara, Time of Day - Python
import time    
    
    local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour #millitary time (0-23)
print(hour)

print("Hello! This program tells you the time of day.")    
hour = int(input("What time is it? (Enter in 24-hour format):\n "))    
    
if hour >= 0 and hour <= 11:    
    print("Good morning!")    
elif hour >= 12 and hour <= 17:    
    print("Good afternoon!")    
else:    
    print("Good evening!")


    print("Hello! This program tells you the time of day.")  
hour = int(input("What time is it? (Enter in 24-hour format):\n "))    
  
if hour >= 0 and hour <= 11:    
    print("Good morning!")    
elif hour >= 12 and hour <= 17:    
    print("Good afternoon!")    
else:    
    print("Good evening!")    