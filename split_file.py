import os
from progress_bar import *

from inputs import get_time_in_seconds

class SplitFile:

    def __init__(self, filename, part_prefix, separator, file_total_duration_seconds, part_duration_seconds, start_part_number, chapters, progress_bar, txt_status):
        self.thread = threading.Thread(target=self.split_file)
        self.doRun = False
        self.filename = filename
        self.part_prefix = part_prefix
        self.separator = separator
        self.file_total_duration_seconds = file_total_duration_seconds
        self.part_duration_seconds = part_duration_seconds
        self.start_part_number = start_part_number
        self.chapters = chapters
        self.progress_bar = progress_bar
        self.txt_status = txt_status
        self.status = []
        self.progress = ProgressBar(file_total_duration_seconds, progress_bar)


    def run(self):
        self.start = datetime.now()

        self.thread.start()

    
    def stop(self):
        self.doRun = True
        self.thread.join()


    def cut_file(self, filename, output_name, start, end, file_extension='mp3'):
        input_path = os.path.abspath(f'Files/{filename}')
        output_path = os.path.abspath(f'Parts/{output_name}.{file_extension}')

        command = f'ffmpeg -y -i {input_path} -ss {start} -t {end - start} -acodec copy {output_path} > /dev/null 2>&1'

        os.system(command)

        self.set_status_text((output_name + "." + file_extension).replace('\\ ', ' '))


    def split_chapter(self, filename, part_prefix, separator, part_suffix, file_total_duration, time_start_file = 0, start_number=1, duration=300): 
        part_number = start_number
        start = time_start_file
        end = time_start_file + duration

        while(end <= file_total_duration):
            output_name = ''.join([part_prefix, '\\ ', separator, '\\ ', str(part_number), '\\ ', separator, '\\ ', part_suffix])
            self.cut_file(filename, output_name, start, end)

            start = end
            end += duration
            part_number += 1

            self.progress.count = start

        if (start < file_total_duration):
            output_name = ''.join([part_prefix, '\\ ', separator, '\\ ', str(part_number), '\\ ', separator, '\\ ', part_suffix])
            self.cut_file(filename, output_name, start, file_total_duration)
            part_number += 1

        return part_number


    def split_file(self):
        part_number = int(self.start_part_number)

        self.progress.run()

        for i in range(0, len(self.chapters) - 1):
            chapter = self.chapters[i]

            chapter_words = chapter.split(' ')
            time_start_file = get_time_in_seconds(chapter_words[0])
            chapter_name = '\\ '.join(chapter_words[1:])

            if i == len(self.chapters) - 2:
                time_end_file = self.file_total_duration_seconds
            else:
                next_chapter = self.chapters[i + 1]
                time_end_file = get_time_in_seconds(next_chapter.split(' ')[0])

            self.set_status_text('Splitting chapter ' + chapter_name.replace('\\ ', ' '))

            part_number = self.split_chapter(self.filename, self.part_prefix, self.separator, chapter_name, time_end_file, time_start_file, part_number, self.part_duration_seconds)

        
        self.set_status_text('Done')
        self.progress.stop()
    

    def set_status_text(self, text):
        self.status.append(text)
        text = '\n'.join(self.status)

        self.txt_status.configure(state='normal')
        self.txt_status.delete(1.0, "end")
        self.txt_status.insert(1.0, text)
        self.txt_status.configure(state='disabled')
        self.txt_status.see('end')