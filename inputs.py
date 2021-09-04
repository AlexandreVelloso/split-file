from datetime import datetime

def filename_has_extension(fileName):
    return '.' in fileName


def get_file_extension(fileName):
    dot_position = fileName.rfind('.')
    return fileName[dot_position+1:]


def read_input(message, default=''):
    value = input(message)

    if (value == ''):
        value = default

    return value


def read_file_name(message):
    filename = input(message)
    file_extension = "mp3"

    if (not filename_has_extension(filename)):
        extension = read_input('Enter the file extension (mp3): ', 'mp3')

        return filename.replace(' ', '\ ') + '.' + file_extension
    
    return filename.replace(' ', '\ ')


def read_time_in_seconds(message, default=''):
    time = read_input(message, default)

    date_time = None
    
    if len(time) == 5:
        date_time = datetime.strptime(time, "%M:%S")
    else:
        date_time = datetime.strptime(time, "%H:%M:%S")

    a_timedelta = date_time - datetime(1900, 1, 1)
    return int(a_timedelta.total_seconds())