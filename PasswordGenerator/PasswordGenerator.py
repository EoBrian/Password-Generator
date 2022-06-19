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
        
        if values['-NUMBER-'] == 8:
            password = apps.generator_pass(8)
            window['-PASSWORD-'].update(password)
        
        elif values['-NUMBER-'] == 9:
            password = apps.generator_pass(9)
            window['-PASSWORD-'].update(password)
        
        elif values['-NUMBER-'] == 10:
            password = apps.generator_pass(10)
            window['-PASSWORD-'].update(password)
        
        elif values['-NUMBER-'] == 11:
            password = apps.generator_pass(11)
            window['-PASSWORD-'].update(password)
        else:
            password = apps.generator_pass(12)
            window['-PASSWORD-'].update(password)

        

    if event == sg.WIN_CLOSED:
        break

window.close()