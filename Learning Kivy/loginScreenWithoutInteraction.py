import kivy
kivy.require('2.2.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout): #Layout Grid
    def __init__(self, **kwargs): #Iniciando o objeto (N sei o que é kwargs)
        super(LoginScreen, self).__init__(**kwargs) #N sei o que é super
        self.cols = 2 #colocar duas colunas
        self.add_widget(Label(text='User Name')) #Adiciona uma label que vai ter o texto Username
        self.username = TextInput(multiline=False) #username vai receber um input de texto que não vai permitir multiline
        self.add_widget(self.username) #Adiciona um widget que tem como base a variável username
        self.add_widget(Label(text='password')) #adiciona uma widget que é uma label com o texto password
        self.password = TextInput(password=True, multiline = False) #adiciona uma variavel que recebe um input de text que não tem multiline e é formatado como uma password
        self.add_widget(self.password) #Transforma a variavel em um widget

class MyApp(App):
    def build(self):
        return LoginScreen()
    

if __name__ == '__main__':
    MyApp().run()