from fileinput import filename
import PySimpleGUI as sg
import os.path

from inputs import get_time_in_seconds
from split_file import *


size_col1 = (25, 0)
col1 = [
    [
        sg.Text('Please select a file', size=size_col1),
        sg.In(key='file_path', size=(20, 1), disabled=True, enable_events=True),
        sg.FileBrowse(initial_folder='./Files', file_types=[('Mp3 files', '*.mp3')]),
    ],

    [
        sg.Text('Enter the first part number', size=size_col1),
        sg.InputText('1', key='part_number', size=(5, 1)),
    ],
    
    [
        sg.Text('Enter the part prefix', size=size_col1),
        sg.InputText('', key='part_prefix', size=(5, 1)),
    ],

    [
        sg.Text('Enter the separator', size=size_col1),
        sg.InputText('-', key='separator', size=(5, 1)),
    ],

    [
        sg.Text('Enter the file duration', size=size_col1),
        sg.InputText('00:00:00', key='file_duration', size=(10, 1)),
    ],

    [
        sg.Text('Enter the part duration', size=size_col1),
        sg.InputText('05:00', key='part_duration', size=(10, 1)),
    ],

    [
        sg.Text('Enter the time of each chapter', size=size_col1),
        sg.Multiline(size=(30, 10), key='chapters'),
    ],

    [
        sg.Button('Split file', key='split_file'),
    ]
]

size_col2 = (8,0)
col2 = [
    [
        sg.Text('Filename', size=size_col2),
        sg.Text(key="show_filename", size=(40,0)),
    ],
    [
        sg.Text('Status', size=size_col2),
        sg.Multiline(key='chapters', size=(40, 25)),
    ],
]

layout = [[
    sg.Column(col1, element_justification='l' ),
    sg.VerticalSeparator(),
    sg.Column(col2, element_justification='l'),
]]


window = sg.Window('Split audio file', layout)


def split():
    filename = values['file_path'].rstrip().replace(' ', '\\ ')
    filename = os.path.basename(filename)

    part_prefix = values['part_prefix']
    separator = values['separator']

    file_total_duration_seconds = get_time_in_seconds(values['file_duration'])
    part_duration_seconds = get_time_in_seconds(values['part_duration'])
    start_part_number = int(values['part_number'])

    chapters = values['chapters'].split('\n')

    part_number = int(start_part_number)

    split_file = SplitFile(filename, part_prefix, separator, file_total_duration_seconds, part_duration_seconds, part_number, chapters)
    split_file.run()


# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "file_path":
        filename = values['file_path']
        print(filename)
        filename = os.path.basename(filename)

        window['show_filename'].update(filename)

    if event == 'split_file':
        filename = values['file_path']

        if filename == '':
            sg.popup('Please select a file')
            continue

        if not os.path.isfile(filename):
            sg.popup('Please select a valid file')
            continue

        split()

window.close()