import pandas as pd
import sqlite3
from sqlite3 import Error
import os


#id, nome, nf, data emissao, data vencimento, tipo de produto


#cria o banco de dados
def db_create(nome):
    file = nome + ".db"
    open(file, "w")
    if os.path.exists(file):
        pass
    create = ''' CREATE TABLE main(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nome VARCHAR(64), 
                            nf INTEGER,
                            dataEmissao VARCHAR(64), 
                            dataVencimento VARCHAR(64),
                            tipo_produto VARCHAR(64)
                            )
            '''
    conn = sqlite3.connect(file)
    conn.execute(create)
    conn.close()
    return file

#conexao geral
def connection(db): 
    try:
        sqlite3.connect(db)
        conn = sqlite3.connect(db)
    except Error as e:
        print(f'{e}, error in connection')
    return conn 

#retorna nome de tabelas
def return_tables(db):
    x = connection(db)
    cursor = x.cursor()
    querry = "SELECT name FROM sqlite_master WHERE type='table';"
    x = cursor.execute(querry)
    data = x.fetchall()
    x.close()
    return data[0]
    
#retorna esquema de tables
def return_schema(db):
    tn = return_tables(db)
    table = tn[0]
    x = rf"PRAGMA table_info('{table}')"
    conn = connection(db)
    cursor = conn.cursor()
    y = cursor.execute(x)
    ls = []
    for i in y:
        ls.append(i[1])
    conn.close()
    return ls

#retorna todos os valores da coluna
def showValues(db):
    table = return_tables(db)
    conn = connection(db)
    cursor = conn.cursor() 
    data = cursor.execute(f'select * from {table[0]}')
    raw = data.fetchall()
    for i in raw:
        print(i)
    conn.close()

#insere dados na sequencia =database(db) nome, nf, dataEmissao, dataVencimento, tipo_produto
def insertAll(db, a, b, c, d, e):
    try:
        table = return_tables(db)
        table_principal = return_schema(db)
        querry = rf'''INSERT INTO {table[0]} ({table_principal[1]}, {table_principal[2]}, {table_principal[3]}, {table_principal[4]}, {table_principal[5]}) VALUES(?, ?, ?, ?, ?)''' 
        param = (str(a), int(b), str(c), str(d), str(e))
        print(querry)
        conn = connection(db)
        cursor = conn.cursor()
        cursor.execute(querry, param)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
    except Exception as e:
        print(e)

#atualiza dados sequencia db = banco para acesso, param1 = coluna; param2 = valor; param3 = id
def updateData(db, param1, param2, param3):
    table = return_tables(db)
    querry = f'update {table} set {param1} = "{param2}" where id = {param3};'
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#nao serve pra retornar dados, mas para executar "PERIGOSO", ordem db = banco pra acesso, querry = comando 
def execute(db, querry):
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#deleta dados pela id , db = banco acesso, param = id para deletar
def delete(db, param):
    execute(f"delete from items where id = {param}")
    conn = connection(db)
    conn.close()

#atualiza o id de certo dado aonde db = banco de acesso, param1 = novo id; param2 = id do dado
def update_id(db, param1, param2):
    querry = f'update items set id = "{param1}" where id = {param2};'
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza o nome de certo dado aonde db = banco de acesso, param1 = novo nome; param2 = id do dado
def update_name(db, param1, param2):
    querry = f'update items set nome = "{param1}" where id = {param2};'
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza a quantidade de certo dado aonde db = banco de acesso, param1 = nova quantidade; param2 = id do dado
def update_quantd(db, param1, param2):
    querry = f'update items set quantidade = "{param1}" where id = {param2};'
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza o parametro comprar de certo dado aonde db = banco de acesso, param1 = nova inf; param2 = id do dado
def update_comprar(db, param1, param2):
    querry = f'update items set comprar = "{param1}" where id = {param2};'
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#retorna tabelas de banco selecionado em formato pandas, db = banco de acesso
def returnPd(db):
    conn = connection(db)
    table = return_tables(db)
    df = pd.read_sql_query(f'select * from {table}', conn)
    conn.close()
    return df

#retorna ids especificos em pandas, db = banco de acesso, id = id
def return_x(db, id):
    table = return_tables(db)
    conn = connection(db)
    df = pd.read_sql_query(f'select * from {table} where id = {id}', conn)
    conn.close()
    return df

#executa querry para retornar tabelas especificas, db = banco de acesso, a = parametro
def insert_especift(db, a):
    table = return_tables()
    insert_schema = return_schema(db)
    querry = f'''insert into {table}({insert_schema[0]}) 
                values(?)''' 
    param = a 
    print(querry)
    conn = connection(db)
    cursor = conn.cursor()
    cursor.execute(querry, param)
    conn.commit()
    conn.close()

#insere dados na sequencia =database(db) nome(char), nf(int), dataEmissao(data), dataVencimento(date), tipo_produto(char)
db_teste = db_create("teste")
insertAll(db_teste, "a", 126, "26/26/2047", "26/26/2047" , "teste")
showValues(db_teste)
