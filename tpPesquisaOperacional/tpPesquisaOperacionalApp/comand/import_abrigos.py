import sqlite3

# Corrigir o caminho do banco de dados
conexao = sqlite3.connect('c:/Users/arthu/OneDrive/Documentos/tp-pesquisa-operacional/tpPesquisaOperacional/tpPesquisaOperacionalApp/dbsqlite3')

# Verificar se a tabela abrigos existe
cursor = conexao.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='abrigos';")

if not cursor.fetchone():
    # Se a tabela abrigos não existir, cria a tabela
    conexao.execute('''
    CREATE TABLE abrigos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        localizacao TEXT,
        capacidade INTEGER
    )
    ''')
    print("Tabela 'abrigos' criada com sucesso.")
else:
    print("A tabela 'abrigos' já existe.")

conexao.close()