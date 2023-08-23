from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

class DialogContent(MDBoxLayout):
    #Abre uma caixa de dialogo que recebe a tarefa do usuário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%a %d %b %y'))
    def show_date_picker(self):
        #Mostra o seletor de data
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()
    def on_save(self, instance, value, date_range):
        #Pega a data do seletor de datas e a converte, é um formulário mais amigável então altera o label da data para esse
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text = str(date)


class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple" #Tema cor primária 

    def show_task_dialog(self):
        if not self.task_list_dialog: #Se não tiver uma tarefa pendente cria uma tarefa
            self.task_list_dialog = MDDialog(
                title='Create Task',
                type ='custom',
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()
    
    def add_task(self, task, task_date):
        #Adicionar uma tarefa
        print(task.text, task_date)
        task.text = '' #Torna a entrada do dalog box uma string vazia

if __name__=="__main__":
    app = MainApp()
    app.run()