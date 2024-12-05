from Database import Database

class Produto:
    def __init__(self) -> None:
        self.nome_produto = None
        self.peso_produto = None
        self.preco_produto = None
        self.descricao_produto = None
        self.marca_produto = None
        self.modelo_produto = None
        self.qnt_produto = None
        self.cor_produto = None
        self.banco = Database()

    def listarProduto(self):
        res = self.banco.selectProduto()
        return res
    
    def listarPorIDProduto(self, id):
        res = self.banco.selectIDProduto(id)
        return res

    def atualizarProduto(self, lista):
        res = self.banco.updateProduto(lista)
        return res
    
    def cadastrarProduto(self, nome, peso, preco, descricao, marca, modelo, quantidade, cor):
        tupla = (nome, peso, preco, descricao, marca, modelo, quantidade, cor)
        self.banco.insertProduto(tupla)
        return True
    
    def excluirProduto(self, id):
        res = self.banco.deleteProduto(id)
        return res