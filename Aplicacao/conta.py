from log import gerador_log
from datetime import date, datetime

class conta:
    agencia = "0001"
    def __init__(self,  conta, usuario):
        self.conta = conta
        self.usuario = usuario

        self.saldo_Conta = 0.00
        self.LIMITE_TRANSACOES = 10
        self.LIMITE_VALOR = 500
        self.quantidade_transacoes={date.today:0}
        self.historico_Conta=[]
        
    def __valida_quantidade_transacoes__(self, realizou_transacao=False ):
        
        if(self.quantidade_transacoes.get(date.today)==None):
            self.quantidade_transacoes[date.today]=0
        
        if realizou_transacao:
            self.quantidade_transacoes.update({date.today: self.quantidade_transacoes.get(date.today)+1}) 
        else:
           if self.quantidade_transacoes.get(date.today) >= self.LIMITE_TRANSACOES:
               return True
           else:
               return False

    @gerador_log
    def deposito(self):
        
        if(self.__valida_quantidade_transacoes__()):
            return "Limite diário de transações atingido, tente novamente outro dia"

        print("Digite o valor que deseja depositar em sua conta: ")
        valor_Depositado = float(input())

        if(valor_Depositado >0):
            print(f"Depositando {valor_Depositado} em sua conta...")
            self.saldo_Conta += valor_Depositado
            self.__valida_quantidade_transacoes__(realizou_transacao=True)
            self.historico_Conta.append(["Deposito", valor_Depositado, datetime.now()])
            return f"Seu deposito de R$ {valor_Depositado} foi realizado com sucesso, seu saldo atual é: {self.saldo_Conta}"
        else:
            return "Valor Digitado inválido."
    
    @gerador_log
    def saque(self):
        
        if(self.__valida_quantidade_transacoes__()):
            return "Limite diário de transações atingido, tente novamente outro dia"
        
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
            self.__valida_quantidade_transacoes__(realizou_transacao=True)
            self.historico_Conta.append(["Saque" ,valor_Sacado, datetime.now()])
            return f"Saque de {valor_Sacado} foi realizado com sucesso, seu saldo atual é: R$ { self.saldo_Conta}"
        else:
            return f"Não foi possível realizar o saque por falta de saldo. Saldo atual: R$ { self.saldo_Conta}"

    

    @gerador_log
    def extrato(self, tipo): 
        print("Extrato da conta: ")

        if(len(self.historico_Conta)==0):
            return "Não houve movimentações."

        for linha in self.historico_Conta:
            if tipo=='Completo':
                print(f"{linha[0]} - R$ {linha[1]} - {linha[2]}")
            else:
                if tipo==linha[0]:
                    print(f"{linha[0]} - {linha[1]} - {linha[2]}")
        return f"Saldo atual: R$ {self.saldo_Conta}"
             

    def __str__(self):

        return f"Agencia: {self.agencia} Conta: {self.conta} Usuario: {self.usuario.__str__()}"