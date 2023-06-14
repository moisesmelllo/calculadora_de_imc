import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('digite sua altura')],
    [sg.Input(key='altura')],
    [sg.Text('digite seu peso')],
    [sg.Input(key='peso')],
    [sg.Button(key='CALCULAR', button_text='CALCULAR'), sg.Button(button_text='limpar', key='limpar')],
    [sg.Text('', key='imc'), sg.Text('', key='situacao')]
]

window = sg.Window('Calculadora de IMC', layout=layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'CALCULAR':
        try:
            peso = float(value['peso'].replace(',', '.'))
            altura = float(value['altura'].replace(',', '.'))
            imc = peso / (altura**2)
            imc = '{:.2f}'.format(imc)
            window['imc'].update(imc)
            imc = float(imc)
            if imc < 18.5:
                window['situacao'].update('sua situacao é magreza')
            elif 18.5 <= imc <= 24.9:
                window['situacao'].update('sua situacao é normal')
            elif 25.0 <= imc <= 29.9:
                window['situacao'].update('sua situacao é sobrepeso')
            elif 30.0 <= imc <= 39.9:
                window['situacao'].update('sua situacao é obesidade')
            else:
                window['situacao'].update('sua situacao é obsidade grave')
        except:
            window['situacao'].update('por gentileza tente novamente!')
    elif event == 'limpar':
        window['peso'].update('')
        window['altura'].update('')
        window['imc'].update('')
        window['situacao'].update('')
