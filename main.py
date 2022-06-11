import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Hello World!')],
            [sg.Button('Ok')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
        break

window.close()