from usuario import Usuario

import os

class Menu:
    @staticmethod
    def menu(lista_usuarios, lista_atas):
        while True:
            Menu.limpar_tela()
            print("Sistema de Gestão de Atas")
            print("1 - Cadastrar Usuários")
            print("2 - Listar Usuários")
            print("3 - Atualizar Usuários")
            print("4 - Excluir Usuário")

            print("7 - Sair")
            opcao = input("Opção: ")
            
            if opcao == '1':
                Menu.cadastrar_usuarios(lista_usuarios)
            elif opcao == '2':
                Menu.listar_usuarios(lista_usuarios)
            elif opcao == '3':
                pass
            elif opcao == '4':
                pass
            elif opcao == '7':
                Menu.limpar_tela()
                print("Obrigado por usar o sistema")
                break
            else:
                print("Opção inválida!!")
                Menu.pegar_tecla('Tecle Enter para continuar...')
                Menu.limpar_tela()
    
    @staticmethod
    def cadastrar_usuarios(lista):
        Menu.limpar_tela()
        print("Cadastro de usuários")
        # matricula, nome, tipo (leitor ou redator), email (CRUD)
        matricula = int(input('Matrícula (Somente números): '))
        nome = input('Nome Completo: ').upper()
        while True:
            t = input('R - Redator; L - Leitor: ')
            t = t.upper()
            if t == 'R':
                tipo = 'Redator'
                break
            elif t == 'L':
                tipo = 'Leitor'
                break
            else:
                print("Escolha R ou L!!")
            
        email = input('Email: ')
        lista.append(Usuario(matricula, nome, tipo, email))
        print('Usuário %s cadastrado com sucesso' % (lista[-1]))
        Menu.pegar_tecla('Tecle Enter para continuar...')
        
    @staticmethod
    def listar_usuarios(lista):
        Menu.limpar_tela()
        print("Listagem de usuários")
        for i in lista:
            print(i)
        
        Menu.pegar_tecla('Tecle Enter para continuar...')


    @staticmethod
    def limpar_tela():
        os.system("cls")
        
    @staticmethod
    def pegar_tecla(texto):
        a = input(texto).split(" ")[0]
        