import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar, Separator, Style
from turtle import width


class MainMenu:
    
    def __init__(self, root):
        self.form_width = 1000
        self.form_height = 400

        self.root = root
        self.root.title('Split audio file')
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        screen_width_resolution = self.root.winfo_screenwidth()
        screen_height_resolution = self.root.winfo_screenheight()

        pos_x = (screen_width_resolution - self.form_width) / 2
        pos_y = (screen_height_resolution - self.form_height) / 2

        self.root.geometry("%dx%d+%d+%d" % (self.form_width, self.form_height, pos_x, pos_y))
        self.root.minsize(self.form_width, self.form_height)

        # Open file row
        self.txt_file_name = StringVar()
        
        self.lb_open_file = Label(self.root, text="Open file", width=10)
        self.ent_file_name = Entry(self.root, width=40, state='readonly', textvariable=self.txt_file_name)
        self.btn_open_file = Button(self.root, text="Open File", command=lambda: self.open_file(self.txt_file_name))
        
        self.lb_open_file.grid(row=0, column=0, sticky=E)
        self.ent_file_name.grid(row=0, column=1, sticky=W)
        self.btn_open_file.grid(row=0, column=2, sticky=W)

        # Part number row
        self.txt_part_number = StringVar(value='1')

        self.lb_part_number = Label(self.root, text="Part number", width=10)
        self.ent_part_number = Entry(self.root, textvariable=self.txt_part_number, width=5)
        
        self.lb_part_number.grid(row=1, column=0, sticky=E)
        self.ent_part_number.grid(row=1, column=1, sticky=W)

        # Part prefix row
        self.txt_part_prefix = StringVar(value='')

        self.lb_part_prefix = Label(self.root, text="Part prefix", width=10)
        self.ent_part_prefix = Entry(self.root, textvariable=self.txt_part_prefix, width=5)

        self.lb_part_prefix.grid(row=2, column=0, sticky=E)
        self.ent_part_prefix.grid(row=2, column=1, sticky=W)

        # Separator row
        self.txt_separator = StringVar(value='-')

        self.lb_separator = Label(self.root, text="Separator", width=10)
        self.ent_separator = Entry(self.root, textvariable=self.txt_separator, width=5)

        self.lb_separator.grid(row=3, column=0, sticky=E)
        self.ent_separator.grid(row=3, column=1, sticky=W)

        # File duration row
        self.txt_file_duration = StringVar(value='00:00:00')

        self.lb_file_duration = Label(self.root, text="File duration", width=10)
        self.ent_file_duration = Entry(self.root, textvariable=self.txt_file_duration, width=10)

        self.lb_file_duration.grid(row=4, column=0, sticky=E)
        self.ent_file_duration.grid(row=4, column=1, sticky=W)

        # Part duration row
        self.txt_part_duration = StringVar(value='05:00')

        self.lb_part_duration = Label(self.root, text="Part duration", width=10)
        self.ent_part_duration = Entry(self.root, textvariable=self.txt_part_duration, width=10)

        self.lb_part_duration.grid(row=5, column=0, sticky=E)
        self.ent_part_duration.grid(row=5, column=1, sticky=W)

        # Chapters row
        self.lb_chapters = Label(self.root, text="Chapters", width=10)
        self.txt_chapters = Text(self.root, width=30, height=10)

        self.scroll_chapters = Scrollbar(self.root, orient=VERTICAL, command=self.txt_chapters.yview)

        self.lb_chapters.grid(row=6, column=0, sticky=E)
        self.txt_chapters.grid(row=6, column=1, sticky=EW)
        self.scroll_chapters.grid(row=6, column=2, sticky='NSW')

        self.txt_chapters['yscrollcommand'] = self.scroll_chapters.set

        # Split file button
        self.btn_split_file = Button(self.root, text="Split file", command=self.split)

        self.btn_split_file.grid(row=7, column=1, sticky=EW)

        # Vertical separator
        self.v_separator = Separator(self.root,orient=VERTICAL)

        self.v_separator.grid(row=0, column=4, padx=10, pady=10, rowspan=8, sticky=NS)

        # Status row
        self.lb_status = Label(self.root, text="Status", width=10)
        self.txt_status = Text(self.root, width=30, height=10)

        self.lb_status.grid(row=0, column=5, sticky=W)
        self.txt_status.grid(row=0, column=6, sticky=EW, rowspan=4)

        # Progress bar row
        self.stl_progress_bar = Style()
        self.stl_progress_bar.theme_use("default")
        self.stl_progress_bar.configure("TProgressbar", thickness=10)

        self.lb_progress_bar = Label(self.root, text="Progress", width=10)
        self.progress_bar = Progressbar(self.root, orient=HORIZONTAL, length=100, style="TProgressbar")

        self.lb_progress_bar.grid(row=4, column=5, sticky=W)
        self.progress_bar.grid(row=4, column=6, sticky=EW)
        self.progress_bar['value'] = 10

    
    def open_file(self, txt_file_name):
        file_path = filedialog.askopenfilename(initialdir='./Files', title="Select file", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))

        if not file_path:
            return

        txt_file_name.set('.../' + os.path.basename(file_path))

        return file_path

    
    def split(self):
        pass


if __name__ == '__main__':
    initial_menu = Tk()

    menu = MainMenu(initial_menu)

    menu.root.mainloop()