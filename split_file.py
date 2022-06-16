import os
from progress_bar import *

from inputs import get_time_in_seconds


def cut_file(filename, output_name, start, end, file_extension='mp3'):
    input_path = os.path.abspath(f'Files/{filename}')
    output_path = os.path.abspath(f'Parts/{output_name}.{file_extension}')

    command = f'ffmpeg -y -i {input_path} -ss {start} -t {end - start} -acodec copy {output_path} > /dev/null 2>&1'

    os.system(command)


def split_chapter(filename, part_prefix, separator, part_suffix, file_total_duration, time_start_file = 0, start_number=1, duration=300): 
    part_number = start_number
    start = time_start_file
    end = time_start_file + duration

    progress = ProgressBar(file_total_duration)
    progress.run()

    while(end <= file_total_duration):
        output_name = ''.join([part_prefix, '\\ ', separator, '\\ ', str(part_number), '\\ ', separator, '\\ ', part_suffix])
        cut_file(filename, output_name, start, end)

        start = end
        end += duration
        part_number += 1

        progress.count = start

    if (start < file_total_duration):
        output_name = ''.join([part_prefix, '\\ ', separator, '\\ ', str(part_number), '\\ ', separator, '\\ ', part_suffix])
        cut_file(filename, output_name, start, file_total_duration)
        part_number += 1

    progress.stop()

    return part_number


def split_file(filename, part_prefix, separator, file_total_duration_seconds, part_duration_seconds, start_part_number, chapters):
    part_number = int(start_part_number)

    for i in range(0, len(chapters)):
        chapter = chapters[i]

        chapter_words = chapter.split(' ')
        time_start_file = get_time_in_seconds(chapter_words[0])
        chapter_name = '\\ '.join(chapter_words[1:])

        if i == len(chapters) - 1:
            time_end_file = file_total_duration_seconds
        else:
            next_chapter = chapters[i + 1]
            time_end_file = get_time_in_seconds(next_chapter.split(' ')[0])

        part_number = split_chapter(filename, part_prefix, separator, chapter_name, time_end_file, time_start_file, part_number, part_duration_seconds)