from banco import obterConta
from saque import sacar
from deposito import depositar

def transferir(contaOri: int, contaDes: float, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaDestino['saldo'] += valor
            contaOrigem['saldo'] -+ valor
            print('Transferência realizada com sucesso!')
        else:
            print('Saldo insuficiente para transferência!')
    else:
        print('Uma das contas não existe!')

# transferir(1, 2, 333)
# print()

