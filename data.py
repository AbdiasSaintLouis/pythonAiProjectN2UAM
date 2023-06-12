import pandas as pd
import pymysql


def load_data(file_name=None, file_type=None, host=None, user=None, password=None, db=None, table=None):
    if file_name is not None and file_type is not None:
        # carregar os dados a partir do arquivo
        if file_type == 'csv':
            data = pd.read_csv(file_name)
        elif file_type == 'xlsx' or file_type == 'xls':
            data = pd.read_excel(file_name)
        elif file_type == 'json':
            data = pd.read_json(file_name)
        # adicione mais elifs para outros tipos de arquivos que você deseja suportar
        else:
            raise ValueError(f"Tipo de arquivo inválido: {file_type}")
    elif host is not None and user is not None and password is not None and db is not None and table is not None:
        # criar uma conexão com o banco de dados
        conn = pymysql.connect(host=host, user=user, password=password, db=db)

        # carregar os dados a partir da tabela
        query = f"SELECT * FROM {table}"
        data = pd.read_sql(query, conn)

        # fechar a conexão
        conn.close()

    else:
        raise ValueError("Você deve especificar um arquivo ou uma conexão com o banco de dados")

    return data

