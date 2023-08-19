from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'Seu saldo é: {cliente["saldo"]}')
    else:
        print('Cliente não encontrado!')

# consultarSaldo(1)