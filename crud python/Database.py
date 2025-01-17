import mysql.connector

class Database:
    def __init__(self, banco='crud_py'):
        self.banco = banco
        self.conn =  None

    def connect(self):
        #definir host, database, user e password // se for no xampp o host e "localhost" e o user e "root"
        self.conn = mysql.connector.connect(host='localhost', database='', user='root', password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            # print("CONECTADO COM SUCESSO!")
            # print()
        else:
            print("ERRO NA CONEXÃO")

    def insertUsuario(self, tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO usuario (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)', tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            print(erro)

    def selectUsuario(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM usuario")
            dados = self.cursor.fetchall()
            return dados

        except Exception as erro:
            print(erro)
    
    def selectIDUsuario(self, id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM usuario WHERE id = {id}")
            dados = self.cursor.fetchone()
            #FORMA DE PRINT
            # print(f"ID: {dados[0]}, NOME: {dados[1]}, CPF: {dados[2]}, EMAIL: {dados[3]}")
            return dados

        except Exception as erro:
            print(erro)

    def deleteUsuario(self, id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM usuario WHERE id = {id}")
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

    def updateUsuario(self, lista):
        self.connect()
        print()
        print(f"LISTA QUE CHEGOU AO BANCO: {lista}")
        try:
            print()
            self.cursor.execute(f""" 
                                UPDATE usuario
                                set nome = '{lista[1]}',
                                cpf = '{lista[2]}',
                                email = '{lista[3]}',
                                senha = '{lista[4]}'
                                WHERE id = {lista[0]}
                                """)
            
            self.conn.commit()
            # return True

        except Exception as erro:
            print(erro)

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print()
            print("CONEXÃO ENCERRADA COM SUCESSO!!!")

#----------------------PRODUTOS--------------------------------------------
    def insertProduto(self, tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO produto (nome_produto, peso_produto, preco_produto, descricao_produto, marca_produto, modelo_produto, qnt_produto, cor_produto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            print(erro)

    def selectProduto(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            dados = self.cursor.fetchall()
            return dados

        except Exception as erro:
            print(erro)

    def selectIDProduto(self, id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id = {id}")
            dados = self.cursor.fetchone()
            #FORMA DE PRINT
            # print(f"ID: {dados[0]}, NOME: {dados[1]}, CPF: {dados[2]}, EMAIL: {dados[3]}")
            return dados

        except Exception as erro:
            print(erro)

    def deleteProduto(self, id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id = {id}")
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

    def updateProduto(self, lista):
        self.connect()
        print(f"LISTA QUE CHEGOU AO BANCO: {lista}")
        try:
            print()
            self.cursor.execute(f""" 
                                UPDATE produto
                                set nome_produro = '{lista[1]}',
                                peso_produto = '{lista[2]}',
                                preco_produto = '{lista[3]}',
                                descricao_produto = '{lista[4]}',
                                marca_produto = '{lista[5]}',
                                modelo_produto = '{lista[6]}',
                                qnt_protudo = '{lista[7]}',
                                cor_produto = '{lista[8]}'
                                WHERE id = {lista[0]}
                                """)
            
            self.conn.commit()
            # return True

        except Exception as erro:
            print(erro)

#TESTE DAS FUNÇÕES
# if __name__ == '__main__':
    # d1 = Database()
    # d1.connect()
    # d1.insert()
    # d1.select()
    # d1.selectID(2)
    # d1.delete(1)
    # d1.select()
    # d1.update()
