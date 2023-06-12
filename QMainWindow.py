# import sys
# from turtle import pd
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFileDialog, QComboBox, \
#     QVBoxLayout, QSlider, QTableView
# from PyQt5.QtGui import QPixmap
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs
#
#
# def pandasModel(data):
#     pass
#
#
# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # definir a janela principal
#         self.setWindowTitle("Aprendizado de Máquina")
#         self.setGeometry(100, 100, 800, 600)
#
#         # criar o widget central
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
#
#         # criar o layout do widget central
#         self.layout = QVBoxLayout()
#         self.central_widget.setLayout(self.layout)
#
#         # criar o botão para carregar o conjunto de dados
#         self.load_data_button = QPushButton("Carregar Dados")
#         self.load_data_button.clicked.connect(self.load_data)
#         self.layout.addWidget(self.load_data_button)
#
#         # criar o menu suspenso para selecionar o algoritmo de clusterização
#         self.algo_combobox = QComboBox()
#         self.algo_combobox.addItems(["K-means", "DBSCAN"])
#         self.layout.addWidget(self.algo_combobox)
#
#         # criar o slider para ajustar o número de clusters
#         self.cluster_slider = QSlider(Qt.Horizontal)
#         self.cluster_slider.setMinimum(2)
#         self.cluster_slider.setMaximum(10)
#         self.cluster_slider.setValue(5)
#         self.cluster_slider.setTickPosition(QSlider.TicksBelow)
#         self.cluster_slider.setTickInterval(1)
#         self.cluster_slider.valueChanged.connect(self.cluster_data)
#         self.layout.addWidget(self.cluster_slider)
#
#     def load_data(self):
#         # abrir uma caixa de diálogo para selecionar o arquivo de dados
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         file_name, _ = QFileDialog.getOpenFileName(self, "Carregar Dados", "",
#                                                    "Arquivos CSV (*.csv);;Todos os Arquivos (*)", options=options)
#         if file_name:
#             # carregar os dados a partir do arquivo selecionado
#             data = pd.read_csv(file_name)
#
#             # exibir os dados em uma tabela
#             self.data_table = QTableView()
#             self.data_table.setModel(pandasModel(data))
#             self.layout.addWidget(self.data_table)
#
#     def cluster_data(self):
#         # obter o número de clusters a partir do slider
#         num_clusters = self.cluster_slider.value()
#
#         # gerar os dados aleatórios
#         X, y = make_blobs(n_samples=100, centers=num_clusters, random_state=42)
#
#         # executar o algoritmo de clusterização selecionado
#         if self.algo_combobox.currentText() == "K-means":
#             kmeans = KMeans(n_clusters=num_clusters)
#             kmeans.fit(X)
#             labels = kmeans.labels_
#         elif self.algo_combobox.currentText() == "DBSCAN":
#             pass  # implementar o DBSCAN
#
#         # exibir a visualização em um gráfico scatter
#         plt.scatter(X[:, 0], X[:, 1], c=labels)
#         plt.show()
