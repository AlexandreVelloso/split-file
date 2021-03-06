import sys
from datetime import datetime
import threading
import time

class ProgressBar:

    def __init__(self, total, progress_bar):
        self.start = datetime.now()
        self.count = 0
        self.total = total
        self.progress_bar = progress_bar
        self.thread = threading.Thread(target=self.update_progress_bar)
        self.doRun = True


    def run(self):
        self.start = datetime.now()
        self.thread.start()


    def stop(self):
        self.doRun = False


    def update_progress_bar(self):
        while(self.count < self.total and self.doRun == True):
            self.progress_bar['value'] = self.remains()
            time.sleep(0.1)

        time.sleep(0.1)       
        self.progress_bar['value'] = self.remains()


    def remains(self):
        return round(100.0 * self.count / float(self.total), 1)
