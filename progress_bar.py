import sys
from datetime import datetime
import threading
import time

class ProgressBar:

    def __init__(self, total, window):
        self.start = datetime.now()
        self.count = 0
        self.total = total
        self.window = window
        self.thread = threading.Thread(target=self.update_progress_bar)
        self.doRun = False


    def run(self):
        self.start = datetime.now()
        self.thread.start()


    def stop(self):
        self.doRun = True
        self.thread.join()


    def update_progress_bar(self):
        while(self.count < self.total and self.doRun == False):
            self.window['progress_bar'].update(self.remains())
            time.sleep(0.1)

        time.sleep(0.1)       
        self.window['progress_bar'].update(self.remains())


    def remains(self):
        return round(100.0 * self.count / float(self.total), 1)
