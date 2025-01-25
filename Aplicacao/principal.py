saldo_Conta = 0.00
LIMITE_SAQUE = 3
LIMITE_VALOR = 500
quantidade_saque=0
historico_Conta=[]

def deposito():
    print("Digite o valor que deseja depositar em sua conta: ")
    valor_Depositado = float(input())

    if(valor_Depositado >0):
        print(f"Depositando {valor_Depositado} em sua conta...")
        global saldo_Conta
        saldo_Conta += valor_Depositado
        historico_Conta.append(f"Deposito - R$ {valor_Depositado}")
        return f"Deposito realizado com sucesso, seu saldo atual é: {saldo_Conta}"
    else:
        return "Valor Digitado inválido."

def saque():
    global saldo_Conta
    global quantidade_saque
    global LIMITE_SAQUE
    global LIMITE_VALOR
    if(quantidade_saque >=LIMITE_SAQUE):
        return "Limite diário de saque atingido, tente novamente outro dia"
    
    if(saldo_Conta==0):
        return "Não será possível realizar o saque por falta de saldo"
    

    print("Digite o valor que deseja sacar: ")
    valor_Sacado = float(input())

    if(valor_Sacado <=0):
        return "Valor digitado inválido"

    if(valor_Sacado > LIMITE_VALOR):
        return "Valor informado maior que limite por saque"

    if(valor_Sacado <= saldo_Conta):
        print(f"Realizando saque de {valor_Sacado}...")
        saldo_Conta-= valor_Sacado
        quantidade_saque +=1
        historico_Conta.append(f"Saque - R$ {valor_Sacado}")
        return f"Saque realizado com sucesso, seu saldo atual é: R$ { saldo_Conta}"
    else:
        return "Não foi possível realizar o saque por falta de saldo."
    

def extrato(): 
    print("Extrato da conta: ")
    if(len(historico_Conta)==0):
        return "Não houve movimentações."
    for linha in historico_Conta:
        print(linha)
    return f"Saldo atual: R$ {saldo_Conta}"

permanecer_Menu=True


while permanecer_Menu:
    #MENU
    print("\n")
    print("### MENU ###")
    print("Digite a opção desejada: ")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3- Extrato")
    print("4 - Sair")
    
    opcao_selecionada = input()
    print("\n")

    match opcao_selecionada:
        case "1":
            print(deposito())
        case "2":
            print(saque())
        case "3":
            print(extrato())
        case "4":
            print("Encerrando programa...")
            permanecer_Menu = False
        case _:
            print("Opção invalida")


