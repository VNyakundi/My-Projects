import time

hours = int(input('how many hours until your alarm?'))
minutes = int(input('how many minutes until your alarm?'))
seconds = int(input('how many seconds until your alarm?'))

hours = hours*6000
minutes = minutes*60

total_time = hours + minutes + seconds
time.sleep(total_time)

print("timer up!")