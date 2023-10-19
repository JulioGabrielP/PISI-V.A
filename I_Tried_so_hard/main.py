from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker

from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox

# Importando a classe Database do arquivo database
from database import Database
# Instanciando a classe Database criando um objeto db
db = Database()

from datetime import datetime

class DialogContent(MDBoxLayout):
     def __init__(self, **kwargs):
          super(). __init__(**kwargs)
          self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")
    
    #Mostra o calendário onde seleciona a data
     def show_date_picker(self):
          date_dialog = MDDatePicker()
          date_dialog.bind(on_save = self.on_save)
          date_dialog.open()
    
    #Mostrando a data
     def on_save(self, instance, value, date_range):
          date = value.strftime("%A %d %B %Y")
          self.ids.date_text.text=str(date)


class ListItemWithCheckBox(TwoLineAvatarIconListItem):
     def __init__(self, pk=None, **kwargs):
          super().__init__(**kwargs)
          self.pk = pk
    
    # Marcando uma tarefa como completa ou incompleta
     def mark(self, check, the_list_item):
        if check.active == True:
               the_list_item.text = '[s]' + the_list_item.text + '[/s]'
               db.mark_task_as_completed(the_list_item.pk)
        else:
             the_list_item.text = str(db.mark_task_as_incompleted(the_list_item.pk))
        
    # Deletando um item da lista
     def delete_item(self, the_list_item):
          self.parent.remove_widget(the_list_item)
          db.delete_task(the_list_item.pk)

class LeftCheckbox(ILeftBody, MDCheckbox):
     pass
        


# MainApp class
class MainApp(MDApp):
    #Flag
    task_list_dialog = None
    # Onde escolhe o tema do aplicativo PS:Não tinha as cores que eu queria TT
    def build(self):
            self.theme_cls.primary_palette = ("Brown")

    # Função para mostrar as tarefas
    def show_task_dialog(self):
         if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title = "Criar Tarefa",
                type = "custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()


    #Função para criar tarefas
    def add_task(self, task, task_date):
         created_task = db.create_task(task.text, task_date )
         self.root.ids['container'].add_widget(ListItemWithCheckBox ( pk =created_task[0], text = '[b]' + created_task[1] + '[/b]', secondary_text = task_date))
         task.text = ''

    # Função pra fechar o dialog
    def close_dialog(self, *args):
         self.task_list_dialog.dismiss()
              

    def on_start(self):
         '''Isso é pra carregar as tarefas salvas e adicionar elas para o MDList widget'''
         completed_tasks, incompleted_tasks = db.get_tasks()

         if incompleted_tasks != []:
              for task in incompleted_tasks:
                   add_task = ListItemWithCheckBox(pk=task[0], text=task[1], secondary_text = task[2])
                   self.root.ids.container.add_widget(add_task)
          
         if completed_tasks != []:
               for task in completed_tasks:
                    add_task = ListItemWithCheckBox(pk = task[0], text ="[s]" + task[1] + "[/s]", secondary_text = task[2])
                    add_task.ids.check.active = True
                    self.root.ids.container.add_widget(add_task)
              

if __name__ == "__main__":
    app = MainApp()
    app.run()