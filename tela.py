from PySimpleGUI import PySimpleGUI as sg
from main import gerar_senha,caracteres

class Tela():
    def __init__(self):
        sg.theme('black')
        #layout
        layout = [
            [sg.Text('Site/software',size=(12,1)),sg.Input(size=(15,1),key=('site_software'))],
            [sg.Text('Email',size=(12,1)),sg.Input(size=(15,1),key=('email'))],
            [sg.Text('Quantidade de caracteres'),sg.Slider(range=(5,40),default_value=(5),orientation=('h'),key=('tamanho_senha'))],
            [sg.Button('Gerar senha')],
            [sg.Output(size=(32,5))]
        
        ]
        #janela
        self.janela = sg.Window('Gerador de senha').layout(layout)
        
    #extraindo dados da tela
    def iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()

            site_software = self.values['site_software']
            email = self.values['email']
            tamanho_senha = self.values['tamanho_senha']

            print(gerar_senha(caracteres,tamanho_senha))

tela = Tela()
tela.iniciar()
