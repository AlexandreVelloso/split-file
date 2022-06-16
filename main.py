from fileinput import filename
import PySimpleGUI as sg
import os.path

file_picker = [
    [
        sg.Text("Please select a file"),
        sg.In(key="file_path", size=(30, 1), enable_events=True),
        sg.FileBrowse(file_types=(("*.mp3"),)),
    ]
]

file_viewer = [
    [sg.Text("File name")],
    [sg.Text(size=(100, 1), key="file_viewer")],
]

split_file_button = [
    [sg.Button("Split file")],
]

layout = [
    [
        file_picker,
        file_viewer,
        split_file_button,
    ]
]

window = sg.Window("Split audio file", layout)

# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "file_path":
        filename = values["file_path"]
        window['file_viewer'].update(filename)

window.close()