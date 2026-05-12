from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class TaskView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas MVC")
        self.setMinimumSize(300, 400)

        # Componentes
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Escribe una nueva tarea...")
        
        self.add_button = QPushButton("Añadir Tarea")
        self.task_list = QListWidget()

        # Añadir al diseño
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)