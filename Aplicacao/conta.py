from log import gerador_log
class conta:
    agencia = "0001"
    def __init__(self,  conta, usuario):
        self.conta = conta
        self.usuario = usuario

        self.saldo_Conta = 0.00
        self.LIMITE_SAQUE = 3
        self.LIMITE_VALOR = 500
        self.quantidade_saque=0
        self.historico_Conta=[]
        
    @gerador_log
    def deposito(self):
        print("Digite o valor que deseja depositar em sua conta: ")
        valor_Depositado = float(input())

        if(valor_Depositado >0):
            print(f"Depositando {valor_Depositado} em sua conta...")
            self.saldo_Conta += valor_Depositado
            self.historico_Conta.append(f"Deposito - R$ {valor_Depositado}")
            return f"Seu deposito de R$ {valor_Depositado} foi realizado com sucesso, seu saldo atual é: {self.saldo_Conta}"
        else:
            return "Valor Digitado inválido."
    
    @gerador_log
    def saque(self):
        if(self.quantidade_saque >=self.LIMITE_SAQUE):
            return "Limite diário de saque atingido, tente novamente outro dia"
        
        if(self.saldo_Conta==0):
            return "Não será possível realizar o saque por falta de saldo"
        

        print("Digite o valor que deseja sacar: ")
        valor_Sacado = float(input())

        if(valor_Sacado <=0):
            return "Valor digitado inválido"

        if(valor_Sacado > self.LIMITE_VALOR):
            return "Valor informado maior que limite por saque"

        if(valor_Sacado <= self.saldo_Conta):
            print(f"Realizando saque de {valor_Sacado}...")
            self.saldo_Conta-= valor_Sacado
            self.quantidade_saque +=1
            self.historico_Conta.append(f"Saque - R$ {valor_Sacado}")
            return f"Saque de {valor_Sacado} foi realizado com sucesso, seu saldo atual é: R$ { self.saldo_Conta}"
        else:
            return f"Não foi possível realizar o saque por falta de saldo. Saldo atual: R$ { self.saldo_Conta}"
        
    @gerador_log
    def extrato(self): 
        print("Extrato da conta: ")
        if(len(self.historico_Conta)==0):
            return "Não houve movimentações."
        for linha in self.historico_Conta:
            print(linha)
        return f"Saldo atual: R$ {self.saldo_Conta}"

    def __str__(self):

        return f"Agencia: {self.agencia} Conta: {self.conta} Usuario: {self.usuario.__str__()}"