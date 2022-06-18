import PySimpleGUI as sg

layout_main = [
    [],
]

window = sg.Window('Password Generator', layout=layout_main)

while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED:
        break

window.close()