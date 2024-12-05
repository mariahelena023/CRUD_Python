from Usuario import Usuario
from Produto import Produto
from Database import Database

usu1 = Usuario()
pro1 = Produto()
dat1 = Database()

while True:
    print("--" * 30)
    print("TIPO DE INSERT")
    print("- Usuário (1)")
    print("- Produto (2)")
    print("- Sair (0)")
    print()
    tipoInsert = int(input("Insira aqui seu tipo de usuário: "))
    print("--" * 30)

    try:
        if tipoInsert == 1:
            while True:
                print("MENU USUÁRIO")
                print("- Listar usuários (1)")
                print("- Listar usuário por ID (2)")
                print("- Atualizar Usuário (3)")
                print("- Cadastrar Usuário (4)")
                print("- Excluir Usuário (5)")
                print("- Sair do MENU USUÁRIO (0)")
                print()
                op = int(input("Insira a função que deseja realizar: "))
                print()

                try:
                    if op == 1:
                        usuarios = usu1.listarUsuario()
                        print("LISTA DE USUÁRIOS")
                        for i in usuarios:
                            print(f"ID: {i[0]}, NOME: {i[1]}, CPF: {i[2]}, EMAIL: {i[3]}, SENHA: {i[4]}")
                        print("--" * 30)
                    
                    elif op == 2:
                        try:
                            id = int(input("Insira o ID do usuário: "))
                            print()
                            usuario = usu1.listarPorIDUsuario(id)

                            if usuario:
                                print("USUÁRIO")
                                print(f"NOME: {usuario[1]}, CPF: {usuario[2]}, EMAIL: {usuario[3]}, SENHA: {usuario[4]}")
                                print("--" * 30)
                            else:
                                print("USUÁRIO NÃO ENCONTRADO!")
                                print("--" * 30)
                        except Exception as erro:
                            print(erro)

                    elif op == 3:
                        usuarios = usu1.listarUsuario()
                        print("--" * 30)
                        print("LISTA DE USUÁRIOS")
                        for i in usuarios:
                            print(f"ID: {i[0]}, NOME: {i[1]}, CPF: {i[2]}, EMAIL: {i[3]}, SENHA: {i[4]}")
                        print()
                        id = int(input("ID do usuário a ser atualizado: "))
                        print()
                        nome = input("Novo Nome: ")
                        cpf = input("Novo CPF: ")
                        email = input("Novo Email: ")
                        senha = input("Nova Senha: ")

                        lista = [id, nome, cpf, email, senha]

                        atualizado = usu1.atualizarUsuario(lista)

                        if atualizado:
                            print()
                            print("ATUALIZADO COM SUCESSO!")
                        else:
                            print()
                            print("FALHA AO ATUALIZAR")

                    elif op == 4:
                        try:
                            nome = input("Nome: ")
                            cpf = input("CPF: ")
                            email = input("Email: ")
                            senha = input("Senha: ")

                            tupla = (nome, cpf, email, senha)

                            if usu1.cadastrarUsuario(nome, cpf, email, senha):
                                print()
                                print("CADASTRADO COM SUCESSO!")
                                print("--" * 30)
                            else:
                                print("FALHA AO CADASTRAR O USUÁRIO")
                        except Exception as erro:
                            print(erro)
                    
                    elif op == 5:
                        usuarios = usu1.listarUsuario()
                        print("LISTA DE USUÁRIOS")
                        for i in usuarios:
                            print(f"ID: {i[0]}, NOME: {i[1]}, CPF: {i[2]}, EMAIL: {i[3]}, SENHA: {i[4]}")
                        print()
                        id = int(input("Insira o ID do usuário a ser excluído: "))
                        usu1.excluirUsuario(id)
                        print()
                        print("EXCLUÍDO COM SUCESSO!")
                        print()

                    elif op == 0:
                        print("VOLTANDO PARA O MENU PRINCIPAL...")
                        break
                    
                except Exception as erro:
                    print(erro)
                         
        elif tipoInsert == 2:
            while True:
                print("MENU PRODUTO")
                print("- Listar produto (1)")
                print("- Listar produto por ID (2)")
                print("- Atualizar produto (3)")
                print("- Cadastrar produto (4)")
                print("- Excluir produto (5)")
                print("- Sair do MENU PRODUTO (0)")
                print()
                op = int(input("Insira a função que deseja realizar: "))
                print()

                try:
                    if op == 1:
                        produtos = pro1.listarProduto()
                        print("LISTA DE PRODUTOS")
                        for i in produtos:
                            print(f"ID: {i[0]}, NOME: {i[1]}, PESO: {i[2]}g, PREÇO: R${i[3]}, DESCRIÇÃO: {i[4]}, MARCA: {i[5]}, MODELO: {i[6]}, QUANTIDADE: {i[7]}, COR: {i[8]}")
                        print("--" * 30)
                    
                    elif op == 2:
                        try:
                            id = int(input("Insira o ID do produto: "))
                            print()
                            produto = pro1.listarPorIDProduto(id)

                            if produto:
                                print("PRODUTO")
                                print(f"NOME: {i[1]}, PESO: {i[2]}g, PREÇO: R${i[3]}, DESCRIÇÃO: {i[4]}, MARCA: {i[5]}, MODELO: {i[6]}, QUANTIDADE: {i[7]}, COR: {i[8]}")
                                print("--" * 30)
                            else:
                                print("PRODUTO NÃO ENCONTRADO!")
                                print("--" * 30)
                        except Exception as erro:
                            print(erro)

                    elif op == 3:
                        produtos = pro1.listarProduto()
                        print("--" * 30)
                        print("LISTA DE PRODUTOS")
                        for i in produtos:
                            print(f"ID: {i[0]}, NOME: {i[1]}, PESO: {i[2]}g, PREÇO: R${i[3]}, DESCRIÇÃO: {i[4]}, MARCA: {i[5]}, MODELO: {i[6]}, QUANTIDADE: {i[7]}, COR: {i[8]}")
                        print()
                        id = int(input("ID do produto a ser atualizado: "))
                        print()
                        nome = input("Novo Nome: ")
                        peso = input("Novo Peso: ")
                        preco = input("Novo Preço: ")
                        descricao = input("Nova Descrição: ")
                        marca = input("Nova Marca: ")
                        modelo = input("Novo Modelo: ")
                        quantidade = input("Nova Quantidade: ")
                        cor = input("Nova Cor: ")

                        lista = [id, nome, peso, preco, descricao, marca, modelo, quantidade, cor]

                        atualizado = pro1.atualizarProduto(lista)

                        if atualizado:
                            print()
                            print("ATUALIZADO COM SUCESSO!")
                        else:
                            print()
                            print("FALHA AO ATUALIZAR")

                    elif op == 4:
                        try:
                            nome = input("Nome: ")
                            peso = input("Peso: ")
                            preco = input("Preço: ")
                            descricao = input("Descrição: ")
                            marca = input("Marca: ")
                            modelo = input("Modelo: ")
                            quantidade = input("Quantidade: ")
                            cor = input("Cor: ")

                            tupla = (nome, peso, preco, descricao, marca, modelo, quantidade, cor)

                            if pro1.cadastrarProduto(nome, peso, preco, descricao, marca, modelo, quantidade, cor):
                                print()
                                print("CADASTRADO COM SUCESSO!")
                                print("--" * 30)
                            else:
                                print("FALHA AO CADASTRAR O PRODUTO")
                        except Exception as erro:
                            print(erro)
                    
                    elif op == 5:
                        produtos = pro1.listarProduto()
                        print("LISTA DE PRODUTOS")
                        for i in produtos:
                            print(f"ID: {i[0]}, NOME: {i[1]}, PESO: {i[2]}g, PREÇO: R${i[3]}, DESCRIÇÃO: {i[4]}, MARCA: {i[5]}, MODELO: {i[6]}, QUANTIDADE: {i[7]}, COR: {i[8]}")
                        print()
                        id = int(input("Insira o ID do produto a ser excluído: "))
                        pro1.excluirProduto(id)
                        print()
                        print("EXCLUÍDO COM SUCESSO!")
                        print()

                    elif op == 0:
                        print("VOLTANDO PARA O MENU PRINCIPAL...")
                        break
                    
                except Exception as erro:
                    print(erro)

        elif tipoInsert == 0:
            dat1.close_connection()
            
    except Exception as erro:
        print(erro)
        print()
        
    