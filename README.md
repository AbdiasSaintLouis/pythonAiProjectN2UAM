# pythonAiProjectN2UAM

Abdias Saint Louis RA: 125111369567

Alan Ataide Coimbra Souza RA: 125111367168


Explicações: 
Este programa é uma aplicação gráfica que permite ao usuário carregar dados de um arquivo CSV, Excel, JSON ou de um banco de dados, exibir os dados em uma tabela e gerar visualizações correspondentes aos dados.
Primeiramente, são importadas as bibliotecas necessárias, como `sys`, `pandas`, `openpyxl`, `PyQt5`, `matplotlib`, `sklearn.cluster`, `sklearn.metrics` e `sklearn.linear_model`.
Em seguida, são definidas três funções para gerar visualizações correspondentes aos dados:
- `plot_scatter`: Esta função realiza o agrupamento com KMeans e plota o gráfico de dispersão correspondente aos dados. A biblioteca `sklearn.cluster` é usada para realizar a clusterização.
- `plot_confusion_matrix`: Esta função realiza a classificação com um modelo de exemplo, calcula a matriz de confusão e plota a matriz de confusão correspondente aos dados. A biblioteca `sklearn.metrics` é usada para calcular a matriz de confusão.
- `plot_regression`: Esta função realiza a regressão linear e plota a linha de regressão correspondente aos dados. A biblioteca `sklearn.linear_model` é usada para realizar a regressão linear.
Em seguida, o programa verifica se o arquivo de dados foi selecionado. Se sim, a função `load_data` do módulo `data.py` é usada para carregar os dados do arquivo e retorná-los como um DataFrame. O DataFrame é então exibido em uma tabela usando a classe `pandasModel` do módulo `pandasModel.py`. Em seguida, o programa verifica o tipo de análise que deve ser realizada e chama uma das três funções de visualização correspondentes.
Se o arquivo de dados não for selecionado, o programa tenta se conectar a um banco de dados usando as informações de conexão fornecidas. Em seguida, a função `load_data` é usada para carregar os dados do banco de dados e retorná-los como um DataFrame. O DataFrame é então exibido em uma tabela usando a classe `pandasModel`. O programa novamente verifica o tipo de análise que deve ser realizada e chama uma das três funções de visualização correspondentes.
Por fim, a interface gráfica do usuário é criada usando a biblioteca PyQt5. A janela principal é criada usando a classe `MainWindow` do módulo `ui.py`. Um botão "Fechar" é adicionado à janela e conectado à função `close`. A janela é exibida usando a função `window.show()`. A aplicação é executada usando a função `app.exec_()`.


