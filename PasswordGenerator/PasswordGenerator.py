import PySimpleGUI as sg
import apps

#Themes aplication colors
sg.theme_background_color('#1d3557')
sg.theme_button_color('#a8dadc')
sg.theme_text_element_background_color('#1d3557')

#menu main aplication
menu_aplication = [['&Menu', ['Save', 'Exit',]]]

#inputs
input_aplication= [
    [[sg.Text('email/site: '), sg.Input(key='-EMAIL-')]],
    [[sg.Text('usuário: '), sg.Input(key='-USER-')]],
]

#valores Combo
valores = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

#Layout main aplication
layout_main = [
    [sg.Menu(menu_aplication, font=('Helvetica', 10))],
    [sg.Input(justification='center', key='-PASSWORD-', size=(30,1)), sg.Combo(valores, default_value=8, key='-NUMBER-')],
    [sg.VPush(), sg.Text('O arquivo foi salvo em \nMEU DOCUMENTOS...', visible=False, key='1'), sg.VPush()],
    [input_aplication],
    [sg.Button('GERAR', key='-BUTTON-', expand_x=True)],    
]

#window main
window = sg.Window('Password Generator', layout=layout_main, font=('Verdana', 15), size=(480, 280))

while True:
    event, values = window.read()

    #gerando senha
    if event == '-BUTTON-':
        window['1'].update(visible=False)
        choice_number = values['-NUMBER-']
        password = apps.generator_pass(int(choice_number))
        window['-PASSWORD-'].update(password)

    #opções do menu
    if event == 'Save':
        apps.save_password(password, values['-EMAIL-'], values['-USER-'])
        window['1'].update(visible=True)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()