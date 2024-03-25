import time


# 20-20-20 rule:
# Every 20 minutes spent using a screen, try to look away at something 
# that is 20 feet away for a total of 20 seconds. This is how long it 
# takes for your eyes to reset and relax.


MINS_TO_SECS = 60

class TimeTracker:

    isinitialised = False
    time_for_alert = 20 # minutes interval
    time_to_resume = 20 # seconds interval

    def __init__(self):
        self.isinitialised = True

    def update_alert_time(self,time):
        self.time_for_alert = time

    def update_resume_time(self, time):
        self.time_to_resume = time

    

    def start_tracker(self, onAlert = None, *cargs, onResume=None, **args):
        prev_time = time.time()
        while(self.isinitialised):
            current_time = time.time()

            if current_time - prev_time > self.time_for_alert * MINS_TO_SECS:
                if onAlert is not None:
                    onAlert(*cargs)

                    time.sleep(self.time_to_resume)
                if onResume is not None:
                    onResume(**args)
                prev_time = current_time

            print("diff = ", current_time - prev_time)
            
            
            time.sleep(abs(self.time_for_alert - self.time_to_resume))
            print("Sleep over for ", abs(self.time_for_alert - self.time_to_resume), "seconds")
            