from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon #Pegando do uix do Kivy e permitindo o uso de Labels

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello There', halign='center',theme_text_color='Custom', #Ou é custom ou as cores disponiveis são Primary Black, Secondary Grey, Hint White and Error Red
                         text_color=(99/255, 128/255 ,13/255, 1), #cor do texto
                         font_style = 'Caption') #tipo de fonte
        icon_label= MDIcon(icon='library-video', halign='center') #Icone
        return icon_label

DemoApp().run() 