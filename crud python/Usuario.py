from Database import Database

class Usuario:
    def __init__(self) -> None:
        self.nome =  None
        self.cpf = None
        self.email = None
        self.senha = None
        self.banco = Database()

    def listarUsuario(self):
        res = self.banco.selectUsuario()
        return res
    
    def listarPorIDUsuario(self, id):
        res = self.banco.selectIDUsuario(id)
        return list(res)

    def atualizarUsuario(self, lista):
        res = self.banco.updateUsuario(lista)
        return list(res)
    
    def cadastrarUsuario(self, nome, cpf, email, senha):
        tupla = (nome, cpf, email, senha)
        self.banco.insertUsuario(tupla)
        return True
    
    def excluirUsuario(self, id):
        res = self.banco.deleteUsuario(id)
        return res