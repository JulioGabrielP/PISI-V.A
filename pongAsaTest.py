import kivy
kivy.require('2.2.1') # replace with your current kivy version !

from kivy.app import App #
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='HELLO THERE'/n "General Kenobi ??")


if __name__ == '__main__':
    MyApp().run()