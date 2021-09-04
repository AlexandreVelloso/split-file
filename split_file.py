import os
import datetime
from inputs import *
from progress_bar import *


def cut_file(filename, output_name, start, end, file_extension="mp3"):
    input_path = os.path.abspath(f"Files/{filename}")
    output_path = os.path.abspath(f"Parts/{output_name}.{file_extension}")

    command = f"ffmpeg -y -i {input_path} -ss {start} -t {end - start} -acodec copy {output_path} > /dev/null 2>&1"

    os.system(command)


def split_file(filename, part_prefix, file_total_duration, start_number=1, duration=300, extension="mp3"):
    input_path = os.path.abspath(filename)
    
    part_number = start_number
    start = 0
    end = duration

    progress_bar = ProgressBar()

    progress_bar.draw_progress_bar(start, file_total_duration)

    while(end <= file_total_duration):
        cut_file(filename, part_prefix + str(part_number), start, end)

        start = end
        end += duration
        part_number += 1

        progress_bar.draw_progress_bar(start, file_total_duration)

    if (start < file_total_duration):
        cut_file(filename, part_prefix + str(part_number), start, end)

    progress_bar.draw_progress_bar(file_total_duration, file_total_duration)


def main():
    print('---- File splitter ----\n')
    print('Please add your file into Files folder. The clipped files will be stored into Parts folder.\n')

    filename = read_file_name('Enter the file name: ')

    start_part_number = read_input('Enter the start part number (default 1): ', 1)

    part_prefix = read_input('Enter a part prefix value: ')
    part_prefix = part_prefix.replace(' ', '\\ ')

    part_duration_seconds = read_time_in_seconds('Enter the duration of the parts (default 05:00): ', '05:00')

    file_total_duration_seconds = read_time_in_seconds('Enter file total duration (e.g. 10:05:20): ')

    confirm_text = f"""\nFile name: {filename}
Start part number: {start_part_number}
Part prefix value: {part_prefix}
Part duration in seconds: {part_duration_seconds}
File total duration in seconds: {file_total_duration_seconds}

Are those values correct? (Y/n): """

    confirm = input(confirm_text)

    if (confirm == 'n' or confirm == 'N'):
        exit()

    print('')
    split_file(filename, part_prefix, file_total_duration_seconds)
    print('')


if __name__ == "__main__":
    main()
