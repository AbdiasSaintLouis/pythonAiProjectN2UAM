from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QWidget
import openpyxl


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # criar a interface gráfica do usuário
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Carregador de Dados")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))

        # criar um layout vertical principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # adicionar um grupo de botões
        self.button_group = QGroupBox("Opções")
        self.button_layout = QHBoxLayout()
        self.button_group.setLayout(self.button_layout)
        self.layout.addWidget(self.button_group)

        # adicionar um botão para carregar dados
        self.load_data_button = QPushButton("Carregar Dados")
        self.load_data_button.clicked.connect(self.load_data)
        self.button_layout.addWidget(self.load_data_button)

    def load_data(self):
        pass
    
