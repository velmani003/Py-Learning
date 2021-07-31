import datetime
from playsound import playsound

alarmH = int(input("Set Hour.."))
alarmM = int(input("Set Minute.."))
amPm = str(input("am or pm..?"))
print("Waiting For An Alarm..", alarmH,alarmM,amPm)
if(amPm=="pm"):
    alarmH=alarmH+12
    while(1==1):
        if(alarmH==datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):
            print("Time to wake up!")
            playsound('./act.mp3')
            break
        
