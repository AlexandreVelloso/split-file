import sys
from datetime import datetime

class ProgressBar:

    def __init__(self):
        self.start = datetime.now()

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

        sys.stdout.write('Generating files: [%s] %s%s ... Remaining time: %s\r' % (bar, percents, '%', self.remains(count, total)))

        sys.stdout.flush()