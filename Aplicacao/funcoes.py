from usuario import usuario
from conta import conta
from log import gerador_log

ultima_conta = 0

@gerador_log
def cadastrar_usuario(cpf):
    print("Digite o nome")
    nome = input()

    print("Digite a data de nascimento")
    data_nascimento = input()

    
    print("Digite o endereco")
    endereco = input()
    
    cadastro = usuario(nome, data_nascimento,  cpf, endereco)
    print("Cadastro realizado com sucesso.")
    
    
    return cadastro

@gerador_log
def cadastrar_conta(id,usuario):
    print("Criando conta...")
    cadastro_conta = conta(id, usuario)
    print("Cadastro realizado com sucesso.")
    return cadastro_conta
