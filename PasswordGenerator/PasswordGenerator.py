import PySimpleGUI as sg
import apps

#Themes aplication colors
sg.theme_background_color('#1d3557')
sg.theme_button_color('#a8dadc')
sg.theme_text_element_background_color('#1d3557')

#Layout main aplication
layout_main = [
    [sg.Text('', expand_x=True, justification='center', key='-PASSWORD-')],
    [sg.VPush()],
    [sg.Slider((1, 20), default_value=8, key='-NUMBER-', orientation='horizontal',font=('Helvetica', 12), expand_x=True)],
    [sg.Button('GERAR', key='-BUTTON-', expand_x=True)],
]

#window main
window = sg.Window('Password Generator', layout=layout_main, size=(300,200), font=('Verdana', 15))

while True:
    event, values = window.read()

    if event == '-BUTTON-':
        choice_number = values['-NUMBER-']
        password = apps.generator_pass(int(choice_number))
        window['-PASSWORD-'].update(password)

    if event == sg.WIN_CLOSED:
        break

window.close()