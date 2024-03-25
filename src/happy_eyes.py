import time
import tkinter as tk

from tkinter import *
from sys import exit


import sched

from camera_access import *

from toast_notifier import Toaster


from time_tracker import TimeTracker

import winsound
import sounddevice as sd
import soundfile as sf

event_schedule = sched.scheduler(time.time, time.sleep)


def popupError(s):
    popupRoot = Tk()
    popupRoot.after(2000, None)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "cyan", command = None)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()



def runner():
    i = 0
    toaster = Toaster("imgs\logo.ico")
    while(True):
        
        time.sleep(5)
        popupError("Pop up notification test - "+str(i)) #persistent dialog box opens, program continues only after box is closed
        toaster.showToast_Notification("Pop up notification test - "+str(i), 10)
        openCamera()
        i += 1
        None
        #event_schedule.enter(30, 1, runner, ())


def notify_user_start(toaster):
    toaster.showToast_Notification("Try to look at something 20 feet away for 20 seconds. Count to twenty", 10)
    startsound = 'res\\sounds\\alerts\\mixkit-double-beep-tone-alert-2868.wav'
    winsound.PlaySound(startsound, winsound.SND_FILENAME)


def notify_user_resume():
    resumesound = 'res\\sounds\\alerts\\mixkit-happy-bells-notification-937.wav'
    winsound.PlaySound(resumesound, winsound.SND_FILENAME)


    


if __name__ == "__main__":
    print("Starting program...")

    #event_schedule.enter(0, 1, runner, ())
    #event_schedule.run()

    t = TimeTracker()
    t.update_alert_time(0.1667)
    toaster = Toaster("imgs\logo.ico")



    t.start_tracker(notify_user_start, toaster, onResume=notify_user_resume)
    


'''data, fs = sf.read(startsound, dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing'''
    

    #runner()
    