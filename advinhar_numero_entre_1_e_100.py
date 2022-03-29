import random
import PySimpleGUI as sg
import time


class AdvinharUmNumero():
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        self.colunas_centralizadas = [
            [sg.Text('QUAL VALOR FOI GERADO?', justification='c', size=(25, 0))],
            [sg.Input(size=(22, 0), key='ValorChute')],
            [sg.Button('CONFIRMAR')],
            [sg.Output(size=(25, 5))]
        ]

        self.layout = [
            [sg.VPush()],
            [sg.Push(), sg.Column(self.colunas_centralizadas, element_justification='c'), sg.Push()],
            [sg.VPush()]
        ]

        # criar uma janela
        self.janela = sg.Window('JOGO DE ADVINHAÇÃO', layout=self.layout, size=(500, 300))

        self.DescobrirNumero()

    def PedirValorAleatorio(self):
        self.valor_testado = input('Qual valor gerado? ')

    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def DescobrirNumero(self):
        # recebe valores
        self.LerValoresDaTela()
        # ação
        if self.evento == 'CONFIRMAR':
            while self.tentar_novamente == True:
                self.valor_testado = self.valores['ValorChute']
                try:
                    if int(self.valor_testado) > self.valor_aleatorio:
                        print('Tente um valor mais baixo!')
                        self.LerValoresDaTela()
                    elif int(self.valor_testado) < self.valor_aleatorio:
                        print('Tente um valor mais alto!')
                        self.LerValoresDaTela()
                    else:
                        print('VALOR CORRETO!')
                        time.sleep(2)
                        self.tentar_novamente = False
                        self.janela.close()

                except:
                    print('Digitar apenas números!')
                    self.DescobrirNumero()


jogo = AdvinharUmNumero()
jogo.Iniciar()
