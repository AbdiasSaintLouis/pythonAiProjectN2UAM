import sys
import openpyxl
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableView, QPushButton
from ui import MainWindow
from data import load_data
from pandasModel import pandasModel


if __name__ == '__main__':
    # criar a aplicação
    app = QApplication(sys.argv)

    # criar a janela da interface gráfica do usuário
    window = MainWindow()

    # adicionar um botão "Fechar" à janela
    close_button = QPushButton("Fechar")
    close_button.clicked.connect(window.close)
    window.layout.addWidget(close_button)

    window.show()

    # carregar dados de um arquivo
    file_name, _ = QFileDialog.getOpenFileName(window, "Carregar Dados", "",
                                               "Arquivos CSV (*.csv);;Arquivos Excel (*.xlsx);;Arquivos JSON (*.json);;Todos os Arquivos (*)")
    if file_name:
        file_type = file_name.split('.')[-1]  # obter a extensão do arquivo
        data = load_data(file_name, file_type)

        # exibir os dados em uma tabela
        data_table = QTableView()
        data_table.setModel(pandasModel(data))
        window.layout.addWidget(data_table)

    # carregar dados de um banco de dados
    else:
        host = 'localhost'
        user = 'myuser'
        password = 'mypassword'
        db = 'mydatabase'
        table = 'mytable'

        data = load_data(host=host, user=user, password=password, db=db, table=table)

        # exibir os dados em uma tabela
        data_table = QTableView()
        data_table.setModel(pandasModel(data))
        window.layout.addWidget(data_table)

    # executar a aplicação
    sys.exit(app.exec_())