import PySimpleGUI as sg
import apps

layout_main = [
    [sg.Text('', key='-PASSWORD-')],
    [sg.Combo((8,9,10,11,12), default_value=8, key='-NUMBER-'), sg.Button('GERAR', key='-BUTTON-')],
]

window = sg.Window('Password Generator', layout=layout_main, size=(200,200))

while True:
    event, values = window.read()
    if event == '-BUTTON-':
        for choice in str(values['-NUMBER-']):
            password = apps.generator_pass(int(choice))
            window['-PASSWORD-'].update(password)

    if event == sg.WIN_CLOSED:
        break

window.close()