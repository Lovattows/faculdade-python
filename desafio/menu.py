from usuario import Usuario
from ata import Ata

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
            print("5 - Cadastrar Ata")
            print("6 - Listar Ata")
            print("7 - Atualizar Ata")
            print("8 - Excluir Ata")
            print("9 - Sair")

            opcao = input("Opção: ")

            if opcao == '1':
                Menu.cadastrar_usuarios(lista_usuarios)
            elif opcao == '2':
                Menu.listar_usuarios(lista_usuarios)
            elif opcao == '3':
                print("Função não implementada")
                Menu.limpar_tela()
            elif opcao == '4':
                print("Função não implementada")
                Menu.limpar_tela()
            elif opcao == '5':
                Menu.cadastrar_atas(lista_atas)
            elif opcao == '6':
                Menu.listar_atas(lista_atas)
            elif opcao == '7':
                print("Função não implementada")
                Menu.limpar_tela()
            elif opcao == '8':
                print("Função não implementada")
                Menu.limpar_tela()
            elif opcao == '9':
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
        print('Usuário %s cadastrado com sucesso' % (nome))
        Menu.pegar_tecla('Tecle Enter para continuar...')

    @staticmethod
    def listar_usuarios(lista):
        Menu.limpar_tela()
        print("Listagem de usuários")
        for i in lista:
            print(i)

        Menu.pegar_tecla('Tecle Enter para continuar...')

    @staticmethod
    def cadastrar_atas(lista):
        Menu.limpar_tela()
        print("Cadastro de atas")
        numero = int(input('Número: '))
        data = input('Data: ')
        hora = input('Hora: ')
        local = input('Local: ')
        pauta = input('Pauta: ')
        redator = input('Redator: ')
        lista_integrantes = input('Integrantes: ')
        texto = input('Nome Completo: ')
        validade = input('Valida: ')
        lista.append(Ata(numero, data, hora, local, pauta, redator, lista_integrantes, texto, validade))
        print('Ata %s cadastrada com sucesso' % (numero))
        Menu.pegar_tecla('Tecle Enter para continuar...')

    @staticmethod
    def listar_atas(lista):
        Menu.limpar_tela()
        print("Listagem de atas")
        for i in lista:
            print(i)

        Menu.pegar_tecla('Tecle Enter para continuar...')

    @staticmethod
    def limpar_tela():
        os.system("cls")

    @staticmethod
    def pegar_tecla(texto):
        a = input(texto).split(" ")[0]
