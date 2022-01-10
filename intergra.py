import PySimpleGUI as sg 

class TelaPython:
    def _init_(self):
        #Layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button()]
        ]

        #janela
        janela = sg.Window("Dados do User").layout(layout)
        #Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()
