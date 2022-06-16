from fileinput import filename
import PySimpleGUI as sg
import os.path

from inputs import get_time_in_seconds
from split_file import split_file

file_picker = [
    [
        sg.Text('Please select a file'),
        sg.In(key='file_path', size=(100, 1), disabled=True),
        sg.FileBrowse(initial_folder='./Files', file_types=[('Mp3 files', '*.mp3')]),
    ]
]

parameters = [
    [
        sg.Text('Enter the first part number'),
        sg.InputText('1', key='part_number', size=(3, 1)),
    ],
    [
        sg.Text('Enter the part prefix'),
        sg.InputText('', key='part_prefix', size=(30, 1)),
    ],
    [
        sg.Text('Enter the separator'),
        sg.InputText('-', key='separator', size=(5, 1)),
    ],
    [
        sg.Text('Enter the file duration'),
        sg.InputText('00:00:00', key='file_duration', size=(10, 1)),
    ],
    [
        sg.Text('Enter the part duration'),
        sg.InputText('05:00', key='part_duration', size=(10, 1)),
    ],
    [
        sg.Text('Enter the time of each chapter'),
        sg.Multiline(size=(30, 10), key='chapters'),
    ]
]

split_file_button = [
    [sg.Button('Split file', key='split_file')],
]

layout = [
    [
        file_picker,
        parameters,
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        split_file_button,
    ]
]

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

    split_file(filename, part_prefix, separator, file_total_duration_seconds, part_duration_seconds, part_number, chapters)


# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

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