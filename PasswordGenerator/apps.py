from random import randint, choice
import os



CHARACTERS = {
    'letras': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'numeros': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '@', '*', '$', '%'],

}

def generator_pass(number=8):
    """
    Password generator!
    number: number of characters to be generated
    """
    password = list()
    for contador in range(0, number):
        rng = randint(0, 3)
        choice_letra_pequena = choice(CHARACTERS['letras'][0:27])
        choice_letra_grande = choice(CHARACTERS['letras'][27:])
        choice_numeros = choice(CHARACTERS['numeros'])

        for letra_pequena, letra_grande, numero in zip(choice_letra_pequena, choice_letra_grande, choice_numeros):
            if rng == 0:
                password.append(numero)
            if rng == 1 or rng == 2:
                password.append(letra_grande)
            elif rng == 3:
                password.append(letra_pequena)

    new_password = ''.join(password)
    return new_password


def pathDir():
    #Pegado diretório padrão do usuário
    informações = os.environ
    usuário = informações['USERPROFILE']

    #pasta download
    return rf'{usuário}\OneDrive\Documentos'


def save_password(password=(12345678), email='Anônimo', usuário='Anônimo'):
    os.chdir(pathDir())
    with open('password.txt', 'a') as file:
        file.write(f'email: {email} \nusuário: {usuário} \npassword: {password} \n\n')
    return file
