from banco import *
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.transferencia import transferir

def menu():
    while True:
        print('-----Sistema bancário------')
        print('1 - Adicionar conta')
        print('2 - Editar conta')
        print('3 - Editar conta')
        print('4 - Apagar conta')
        print('5 - Listar contas')
        print('6 - Atualizar nome')
        print('7 - Atualizar saldo')
        print('8 - Realizar saque')
        print('9 - Realizar deposito')
        print('10 - consultar saldo')
        print('11 - Transferência')
        print('12 - Sair')
        opcao = int('Selecione uma opção: ')