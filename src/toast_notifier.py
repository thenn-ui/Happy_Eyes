from win10toast import ToastNotifier
import time


class Toaster:
    
    toaster = None
    isinitialised = False
    iconloc = None

    def __init__(self, iconlocation):
        # One-time initialization
        self.toaster = ToastNotifier()
        self.isinitialised = True
        self.iconloc = iconlocation

    def showToast_Notification(self, message, dur):
        # Show notification whenever needed
        self.toaster.show_toast("Notification!", message, threaded=True, icon_path=self.iconloc)

        # To check if any notifications are active,
        # use `toaster.notification_active()`
        #while self.toaster.notification_active():
            #time.sleep(1)


