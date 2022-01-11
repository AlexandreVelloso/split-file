import os
from inputs import *
from progress_bar import *


def cut_file(filename, output_name, start, end, file_extension="mp3"):
    input_path = os.path.abspath(f"Files/{filename}")
    output_path = os.path.abspath(f"Parts/{output_name}.{file_extension}")

    command = f"ffmpeg -y -i {input_path} -ss {start} -t {end - start} -acodec copy {output_path} > /dev/null 2>&1"

    os.system(command)


def split_file(filename, part_prefix, part_suffix, file_total_duration, time_start_file = 0, start_number=1, duration=300): 
    part_number = start_number
    start = time_start_file
    end = time_start_file + duration

    progress = ProgressBar(file_total_duration)
    progress.run()

    while(end <= file_total_duration):
        cut_file(filename, part_prefix + str(part_number) + part_suffix, start, end)

        start = end
        end += duration
        part_number += 1

        progress.count = start

    if (start < file_total_duration):
        cut_file(filename, part_prefix + str(part_number) + part_suffix, start, file_total_duration)

    progress.stop()

def main():
    print('---- File splitter ----\n')
    print('Please add your file into Files folder. The clipped files will be stored into Parts folder.\n')

    filename = read_file_name('Enter the file name: ')

    start_part_number = int(read_input('Enter the start part number (default 1): ', 1))

    part_prefix = read_input('Enter a part prefix value: ')
    part_suffix = read_input('Enter a suffix: ', '')

    part_prefix = part_prefix.replace(' ', '\\ ') + '\\ '
    part_suffix = '\\ ' + part_suffix.replace(' ', '\\ ')

    time_start_file = read_time_in_seconds('Enter the time to start cutting (default 00:00): ', '00:00')
    file_total_duration_seconds = read_time_in_seconds('Enter file total duration (e.g. 10:05:20): ')
    part_duration_seconds = read_time_in_seconds('Enter the duration of the parts (default 05:00): ', '05:00')

    confirm_text = f"""\nFile name: {filename}
Start part number: {start_part_number}
Part prefix value: {part_prefix}
Part suffix value: {part_suffix}
Time to start cutting: {time_start_file}
File total duration in seconds: {file_total_duration_seconds}
Part duration in seconds: {part_duration_seconds}

Are those values correct? (Y/n): """

    confirm = input(confirm_text)

    if (confirm == 'n' or confirm == 'N'):
        exit()

    print('')
    split_file(filename, part_prefix, part_suffix, file_total_duration_seconds, time_start_file, start_part_number, part_duration_seconds)


if __name__ == "__main__":
    main()
