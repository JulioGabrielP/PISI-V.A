import kivy
from kivy.app import App 
from kivy.uix.label import Label

class KivyHelloApp (App):
    def build (self):
        return Label(text='Hello World !')
    
KivyHelloApp().run()