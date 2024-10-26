import datetime
from playsound import playsound
alarmHour=int(("Enter Hour: "))
alarmMin=int(("Enter Minutes:"))
alarmAm=input("pm/am: ")

if alarm=="pm":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing....")
        playsound("punky.mp3")
        break
