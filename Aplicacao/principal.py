from log import gerador_log
from conta import conta
from funcoes import *
idUsuario=0
idConta=0
permanecer_Menu=True
usuarios = {}
contas = {}



def selecionarConta():
    print("Lista de contas")
    for chave in contas:
        print(f"{chave} - {contas[chave].__str__()}")
    print("0 - Encerrar aplicação")
    print("Qual conta deseja acessar")
    chave_conta = int(input())

    if chave_conta == 0:
        print("Encerrando a aplicação...")
        global permanecer_Menu
        global permanecer_subMenu
        permanecer_Menu = False
        permanecer_subMenu = False
    else:
        if chave_conta in contas:
            print("Acessando conta...")
            subMenu(contas[chave_conta])
        else:
            print("Opção inválida")
            selecionarConta()

#Submenu
def subMenu(contaSelecionada):
    permanecer_subMenu = True
    while permanecer_subMenu:    
        print("### MENU ###")
        print("Digite a opção desejada: ")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair da conta")
        print("5 - Encerrar aplicação")
        
        opcao_selecionada = input()
        print("\n")

        match opcao_selecionada:
            case "1":
                print(contaSelecionada.deposito())
            case "2":
                print(contaSelecionada.saque())
            case "3":
                print(contaSelecionada.extrato())
            case "4":
                print("Retornando ao menu anterior...")
                permanecer_subMenu = False
                global permanecer_Menu
                permanecer_Menu = True
                menu()
            case "5":
                print("Encerrando aplicação...")
                permanecer_Menu = False
                permanecer_subMenu = False
            case _:
                print("Opção invalida")


def menu():
    global permanecer_Menu
    global idUsuario
    global idConta
    global usuarios
    global contas
    #MENU
    while permanecer_Menu:

        print("\n")
        print("### MENU ###")
        print("Digite a opção desejada: ")
        print("1 - Cadastrar usuário")
        print("2 - Cadastrar conta")
        print("3 - Acessar conta")
        print("4 - Encerrar aplicação")

        opcao_selecionada = input()
        print("\n")

        match opcao_selecionada:
            case "1":
                print("Digite o CPF do usuario (Apenas numeros)")
                cpf = input()
                cpf_duplicado=False
                if(len(usuarios)>0):
                    
                    for chave in usuarios:
                        if usuarios[chave].cpf == cpf:
                            cpf_duplicado = True
                if cpf_duplicado:
                    print("Já há um cadastro com esse CPF.")
                else:
                    idUsuario +=1
                    usuarios[idUsuario]=cadastrar_usuario(cpf)
            case "2":
                if len(usuarios)==0:
                    print("Não há usuários cadastrados, primeiro cadastre um usuário.")
                else:
                    print("Lista de usuarios:")
                    for chave in usuarios:
                        print(f"{chave} - {usuarios[chave].__str__()}")
                    print()
                    print("Indique o usuario da conta")
                    usuario_conta = int(input())
                    if usuario_conta in usuarios:
                        print("aqui")
                        idConta +=1
                        contas[idConta]= cadastrar_conta(idConta, usuarios[usuario_conta])
                    else:
                        print("estou no else")
            case "3":
                if len(contas)==0:
                    print("Não há contas cadastradas, primeiro cadastre uma conta.")
                else:
                    selecionarConta()
                    permanecer_Menu = False
            case "4":
                print("Encerrando programa...")
                permanecer_Menu = False
            case _:
                print("Opção invalida")

if permanecer_Menu:
    menu()

