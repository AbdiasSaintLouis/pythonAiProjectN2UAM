import sys
import pandas as pd

import openpyxl
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableView, QPushButton
from ui import MainWindow
from data import load_data
from pandasModel import pandasModel
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression


def plot_scatter(data):
    """
    Realiza o agrupamento com KMeans e plota o gráfico de dispersão.
    """
    # realizar o agrupamento com KMeans
    model = KMeans(n_clusters=3)
    model.fit(data)

    # plotar o gráfico de dispersão
    plt.scatter(data[:, 0], data[:, 1], c=model.labels_)
    plt.show()


def plot_confusion_matrix(data):
    """
    Realiza a classificação com um modelo de exemplo, calcula a matriz de confusão e plota a matriz de confusão.
    """
    # realizar a classificação com um modelo de exemplo
    y_true = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    y_pred = [0, 1, 1, 0, 2, 1, 0, 1, 2]

    # calcular a matriz de confusão
    cm = confusion_matrix(y_true, y_pred)

    # plotar a matriz de confusão
    plt.matshow(cm)
    plt.colorbar()
    plt.show()


def plot_regression(data):
    """
    Realiza a regressão linear e plota a linha de regressão.
    """
    # converter o array numpy para um DataFrame do pandas
    data = pd.DataFrame(data)

    # remover as linhas com valores NaN
    data = data.dropna()

    # verificar se há linhas suficientes
    print('Número de linhas do conjunto de dados: ', data.shape[0])

    # realizar a regressão linear
    X = data.iloc[:, 0].values.reshape(-1, 1)
    y = data.iloc[:, 1].values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    # plotar a linha de regressão
    plt.scatter(X, y)
    plt.plot(X, model.predict(X), color='red')
    plt.show()


if __name__ == '__main__':
    # criar a aplicação
    app = QApplication(sys.argv)

    # criar a janela da interface gráfica do usuário
    window = MainWindow()

    # adicionar um botão "Fechar" à janela
    close_button = QPushButton("Fechar")
    close_button.clicked.connect(window.close)
    window.layout.addWidget(close_button)

    # carregar dados de um arquivo
    file_name, _ = QFileDialog.getOpenFileName(window, "Carregar Dados", "",
                                               "Arquivos CSV (*.csv);;Arquivos Excel (*.xlsx);;Arquivos JSON (*.json);;Todos os Arquivos (*)")
    if file_name:
        file_type = file_name.split('.')[-1]  # obter a extensão do arquivo
        data = load_data(file_name, file_type)

        # exibir os dados em uma tabela
        dataTable = QTableView()
        dataTable.setModel(pandasModel(data))
        window.layout.addWidget(dataTable)

        # verificar o tipo de análise e gerar a visualização correspondente
        if len(data.columns) == 2:
            # agrupamento
            plot_scatter(data.values)
        elif len(data.columns) > 2 and 'class' in data.columns:
            # classificação
            plot_confusion_matrix(data['class'])
        elif len(data.columns) > 2:
            # regressão
           plot_regression(data.values)

    # carregar dados de um banco de dados
    else:
        host = 'localhost'
        user = 'myuser'
        password = 'mypassword'
        db = 'mydatabase'
        table = 'mytable'

        data = load_data(host=host, user=user, password=password, db=db, table=table)

        # exibir os dados em uma tabela
        dataTable = QTableView()
        dataTable.setModel(pandasModel(data))
        window.layout.addWidget(dataTable)

        # verificar o tipo de análise e gerar a visualização correspondente
        if len(data.columns) == 2:
            # agrupamento
            plot_scatter(data.values)
        elif len(data.columns) > 2 and 'class' in data.columns:
            # classificação
            plot_confusion_matrix(data['class'])
        elif len(data.columns) > 2:
            # regressão
            plot_regression(data.values)

    window.show()

    # executar a aplicação
    sys.exit(app.exec_())
