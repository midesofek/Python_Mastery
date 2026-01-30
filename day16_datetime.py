from datetime import datetime, date, time

# print(dir(datetime))
now = datetime.now() ## 2026-01-26 00:42:24.474041
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

## Formatting date time using strftime method
t = now.strftime("%H:%M:%S")
print("time:", t)  
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time one:", time_one)
print("time two:", time_two)

## format str to time using strptime
date_string = "5 December, 2019"
print("date_string =", date_string) 
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

## Using date from datetime
d = date(2026,1,1)
print(d)
print('Current date:', d.today()) 


## Using time from datetime
a = time()
print("a =", a) 
b = time(10, 30, 50)
print("b =", b) 