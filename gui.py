import PySimpleGUI as sg
from challenge import challenge
from fake_data import fake_data


def tela_inicial():
    sg.change_look_and_feel('DarkGreen')
    FILENAME = r'./assets/logo-sicredi-icon-1024.png'
    DISPLAY_TIME_MILLISECONDS = 4000
    sg.Window('', [[sg.Image(FILENAME)]],
              transparent_color=sg.theme_background_color(),
              no_titlebar=True,
              keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)

    tela_layout = [
        [sg.Text('Selecione a ferramenta desejada: ')],
        [sg.Text('________________________________________________________')],
        [sg.Text('          Executar RPA Challenge___________________'),
            sg.Button('Ok', key="select_rpa")],
        [sg.Text('          Coletar dados do FakeData: ________________'),
            sg.Button('Ok', key="select_fake")],

        [sg.Button('Sair')]
    ]
    tela_inicio = sg.Window("RPA Challenge - Sicredi").layout(tela_layout)

    while True:
        event, values = tela_inicio.Read()
        if event in ('Sair', sg.WIN_CLOSED):
            break
        elif event == 'select_rpa':
            tela_challenge()
        elif event == 'select_fake':
            fake_data()

    tela_inicio.close()


def tela_challenge():
    sg.change_look_and_feel('DarkGreen')
    tela_layout = [
        [sg.Text('Arquivo a ser utilizado: '),
            sg.Input(key='file')],
        [sg.Button('Ok')]
    ]
    tela = sg.Window("RPA Challenge - Sicredi").layout(tela_layout)

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSED):
            break
        elif event == 'Ok':
            arquivo = './assets/' + values['file']
            if arquivo == './assets/':
                tela_alert()
            else:
                challenge(arquivo)
            break
    tela.close()


def tela_alert():
    sg.change_look_and_feel('DarkGreen')
    tela_layout = [
        [sg.Text('Por favor informe o nome do arquivo')],
        [sg.Button('Ok')]
    ]
    tela = sg.Window("RPA Challenge - Sicredi").layout(tela_layout)

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSED) or (event == 'Ok'):
            break
    tela.close()


tela_inicial()
