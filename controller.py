class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Conectar el botón de la vista con la función del controlador
        self.view.add_button.clicked.connect(self.add_task_to_model)

    def add_task_to_model(self):
        task_text = self.view.task_input.text()
        if self.model.add_task(task_text):
            self.view.task_list.addItem(task_text)
            self.view.task_input.clear()