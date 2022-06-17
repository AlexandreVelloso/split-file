import os
from tkinter import *
from tkinter import filedialog
from turtle import width


class MainMenu:
    
    def __init__(self, root):
        self.form_width = 500
        self.form_height = 350

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
        txt_file_name = StringVar()
        
        lb_open_file = Label(self.root, text="Open file", width=10)
        ent_file_name = Entry(self.root, width=30, state='disabled', textvariable=txt_file_name)
        btn_open_file = Button(self.root, text="Open File", command=lambda: self.open_file(txt_file_name))
        
        lb_open_file.grid(row=0, column=0, sticky=E)
        ent_file_name.grid(row=0, column=1, sticky=W)
        btn_open_file.grid(row=0, column=2, sticky=W)

        # Part number row
        txt_part_number = StringVar(value='1')

        lb_part_number = Label(self.root, text="Part number", width=10)
        ent_part_number = Entry(self.root, textvariable=txt_part_number, width=5)
        
        lb_part_number.grid(row=1, column=0, sticky=E)
        ent_part_number.grid(row=1, column=1, sticky=W)

        # Part prefix row
        txt_part_prefix = StringVar(value='')

        lb_part_prefix = Label(self.root, text="Part prefix", width=10)
        ent_part_prefix = Entry(self.root, textvariable=txt_part_prefix, width=5)

        lb_part_prefix.grid(row=2, column=0, sticky=E)
        ent_part_prefix.grid(row=2, column=1, sticky=W)

        # Separator row
        txt_separator = StringVar(value='-')

        lb_separator = Label(self.root, text="Separator", width=10)
        ent_separator = Entry(self.root, textvariable=txt_separator, width=5)

        lb_separator.grid(row=3, column=0, sticky=E)
        ent_separator.grid(row=3, column=1, sticky=W)

        # File duration row
        txt_file_duration = StringVar(value='00:00:00')

        lb_file_duration = Label(self.root, text="File duration", width=10)
        ent_file_duration = Entry(self.root, textvariable=txt_file_duration, width=10)

        lb_file_duration.grid(row=4, column=0, sticky=E)
        ent_file_duration.grid(row=4, column=1, sticky=W)

        # Part duration row
        txt_part_duration = StringVar(value='05:00')

        lb_part_duration = Label(self.root, text="Part duration", width=10)
        ent_part_duration = Entry(self.root, textvariable=txt_part_duration, width=10)

        lb_part_duration.grid(row=5, column=0, sticky=E)
        ent_part_duration.grid(row=5, column=1, sticky=W)

        # Chapters row
        lb_chapters = Label(self.root, text="Chapters", width=10)
        ent_chapters = Text(self.root, width=30, height=10)

        scroll_chapters = Scrollbar(self.root, orient=VERTICAL, command=ent_chapters.yview)

        lb_chapters.grid(row=6, column=0, sticky=E)
        ent_chapters.grid(row=6, column=1, sticky=EW)
        scroll_chapters.grid(row=6, column=2, sticky='NSW')

        ent_chapters['yscrollcommand'] = scroll_chapters.set

        # Split file button
        btn_split_file = Button(self.root, text="Split file", command=self.split)

        btn_split_file.grid(row=7, column=1, sticky=EW)

    
    def open_file(txt_file_name):
        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        txt_file_name.set('.../' + os.path.basename(file_path))

        return file_path

    
    def split():
        pass


if __name__ == '__main__':
    initial_menu = Tk()

    menu = MainMenu(initial_menu)

    menu.root.mainloop()