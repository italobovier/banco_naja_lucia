from datetime import date

# Função para exibir o menu principal
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{"="*0}')
    print(f'BANCO NAJA LÚCIA | {dia:02d}/{mes:02d}/{ano}')
    print(f'{"="*50}\n')
    print('1 - Criar Conta')
    print('2 - Entrar na Conta')
    print('3 - Exibir Correntistas')
    print('4 - Excluir Conta')
    print('5 - Encerrar Programa')

# Função para exibir operações disponíveis
def exibir_operacoes():
    print('\nOPERAÇÕES\n')
    print('1 - Consultar Saldo')
    print('2 - Depositar Valor')
    print('3 - Sacar Valor')
    print('4 - Voltar')

# Função para exibir dados do correntista
def exibir_dados(nome, i, saldo):
    print(f'ID: {i}')
    print(f'Nome: {nome}')
    print(f'Agência: 1001{i:02d}')
    print(f'Saldo: R$ {saldo:,.2f}')

# Função para depositar valor
def depositar_valor(saldo, valor):

    # Adiciona um valor ao saldo atual.
   
    if valor > 0:
        saldo += valor
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo

# Função para sacar valor
def sacar_valor(saldo, valor):

#   Subtrai um valor do saldo atual.
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente.")
    else:
        print("O valor do saque deve ser positivo.")
    return saldo
