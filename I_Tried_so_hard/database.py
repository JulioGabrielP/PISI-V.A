import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()
        self.create_task_table()
    #Cria a tabela de tarefas
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, due_date varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0,1))) ")
        self.con.commit()
    
    #Criando as tarefas
    def create_task(self, task, due_date = None):
        self.cursor.execute("INSERT INTO tasks(task, due_date, completed)VALUES(?, ?, ?)", (task, due_date, 0))
        self.con.commit()

        # Selecionando o último item adicionado para poder colocar na lista de tarefas
        created_task = self.cursor.execute('SELECT id, task, due_date FROM tasks WHERE task = ? and completed = 0', (task,)).fetchall()
        return created_task[-1]
    
    #Pegando as Tarefas
    def get_tasks(self):
        ''' Pegando todas as tarefas: Completas e Incompletas'''
        incompleted_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 0").fetchall()
        completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        return completed_tasks, incompleted_tasks
    
    #Update de tarefas
    def mark_task_as_completed(self, taskid):
        '''Marca tarefa como completa'''
        self.cursor.execute("UPDATE tasks SET completed =1 WHERE id = ?", (taskid,))
        self.con.commit()

    def mark_task_as_incompleted(self, taskid):
        '''Marca tarefa como incompleta'''
        self.cursor.execute("UPDATE tasks SET completed =0 WHERE id = ?", (taskid,))
        self.con.commit()

        # retorna o texto da tarefa
        task_text = self.cursor.execute("SELECT task FROM tasks WHERE id = ?", (taskid,)).fetchall()
        return task_text[0][0]
    
    #Deletando as tarefas
    def delete_task(self, taskid):
        '''Deletar uma tarefa'''
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (taskid,))
        self.con.commit()

    #Fechando conexões
    def close_db_connection(self):
        self.con.close()

        