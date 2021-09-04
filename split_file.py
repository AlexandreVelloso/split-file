import os
import datetime
import sys


def filename_has_extension(fileName):
    return '.' in fileName


def get_file_extension(fileName):
    dot_position = fileName.rfind('.')
    return fileName[dot_position+1:]


def read_input(message, default):
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
        date_time = datetime.datetime.strptime(time, "%M:%S")
    else:
        date_time = datetime.datetime.strptime(time, "%H:%M:%S")

    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    return int(a_timedelta.total_seconds())


def cut_file(filename, output_name, start, end, file_extension="mp3"):
    input_path = os.path.abspath(f"Files/{filename}")
    output_path = os.path.abspath(f"Parts/{output_name}.{file_extension}")

    command = f"ffmpeg -y -i {input_path} -ss {start} -t {end - start} -acodec copy {output_path} > /dev/null 2>&1"

    os.system(command)


def split_file(filename, file_total_duration, start_number=1, duration=300, extension="mp3"):
    input_path = os.path.abspath(filename)
    
    part_number = start_number
    start = 0
    end = duration

    draw_progress_bar(start, file_total_duration)

    while(end <= file_total_duration):
        cut_file(filename, str(part_number), start, end)

        start = end
        end += duration
        part_number += 1

        draw_progress_bar(start, file_total_duration)

    if (start < file_total_duration):
        cut_file(filename, str(part_number), start, end)

    draw_progress_bar(file_total_duration, file_total_duration)


def draw_progress_bar(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('Generating files: [%s] %s%s ...%s\r' % (bar, percents, '%', status))

    sys.stdout.flush()


def main():
    print('---- File splitter ----\n')
    print('Please add your file into Files folder. The clipped files will be stored into Parts folder.\n')

    filename = read_file_name('Enter the file name: ')
    start_part_number = read_input('Enter the start part number (default 1): ', 1)
    part_duration_seconds = read_time_in_seconds('Enter the duration of the parts (default 05:00): ', '05:00')
    file_total_duration_seconds = read_time_in_seconds('Enter file total duration (e.g. 10:05:20): ')

    confirm_text = f"""\nFile name: {filename}
Start part number: {start_part_number}
Part duration in seconds: {part_duration_seconds}
File total duration in seconds: {file_total_duration_seconds}

Are those values correct? (Y/n): """

    confirm = input(confirm_text)

    if (confirm == 'n' or confirm == 'N'):
        exit()

    print('')
    split_file(filename, file_total_duration_seconds)


if __name__ == "__main__":
    main()
