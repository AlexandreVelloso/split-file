from datetime import datetime


def get_time_in_seconds(time):
    date_time = None

    if(len(time) == 4):
        time = time.rjust(5, '0')

    if len(time) == 5:
        date_time = datetime.strptime(time, '%M:%S')
    else:
        date_time = datetime.strptime(time, '%H:%M:%S')

    a_timedelta = date_time - datetime(1900, 1, 1)
    return int(a_timedelta.total_seconds())