from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

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
        self.root.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+ '[/b]', secondary_text=task_date))
        task.text = ' ' #Torna a entrada do dialog box uma string vazia

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
        self.ids.date_text.text  = str(date)

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Lista de item customizavel'''

    def __init__(self, pk=None,**kwargs):
        super().__init__(**kwargs)
        #indica o pk que usaremos para vincular os itens da lista às chaves primárias do banco de dados'''
        self.pk = pk
    def mark(self, check, the_list_item):
        '''Marca as tarefas como completas ou incompletas'''
        if check.active == True:
            #Adiciona uma linha no texto se a caixa estiver ativa'
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
        else:
            #'adicionar um código que remova a linha mais tarde
            pass
    def delete_item(self, the_list_item):
        '''Deleta as tarefas'''
        self.parent.remove_widget(the_list_item)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Ícone customizável  na esquerda'''

if __name__=="__main__":
    app = MainApp()
    app.run()

    
