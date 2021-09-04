import sys
from datetime import datetime
import threading

import time

class ProgressBar:

    def __init__(self, total):
        self.start = datetime.now()
        self.count = 0
        self.total = total

    def run(self):
        self.start = datetime.now()

        t = threading.Thread(target=self.update_progress_bar)
        t.start()

    def update_progress_bar(self):
        while(self.count < self.total):
            self.draw_progress_bar(self.count, self.total)
            time.sleep(0.5)

        time.sleep(0.1)
        self.draw_progress_bar(self.total, self.total)
        print('\nFinished')

    def remains(self, done, total):
        if(done <= 0):
            done = 0.1

        now  = datetime.now()
        left = (total - done) * (now - self.start) / done
        sec = int(left.total_seconds())

        if sec < 60:
            return "{} seconds".format(sec)
        else:
            return "{} minutes".format(int(sec / 60))


    def draw_progress_bar(self, count, total):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '█' * filled_len + '-' * (bar_len - filled_len)

        # Clear the buffer
        sys.stdout.write('\x1b[1K\r')
        sys.stdout.write('Generating files: [%s] %s%s ... Remaining time: %s' % (bar, percents, '%', self.remains(count, total)))

        sys.stdout.flush()