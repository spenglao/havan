"""
Essa é uma calculadora escrita em python que converte valores simulando uma casa de câmbio.
Para isso é necessário informar os seguintes dados:
Moeda de origem
Moeda de destino
Cotação do dia
Valor da troca
"""

def converter(valor, cotação):
    """
    Função que calcula a quantidade de moeda de destino com base na cotação do dia e quantidade de moeda de origem.
    """
    return float(valor/cotação)

print('Seja bem vindo ao Havan Exchange! \n')

def menu():
    """
    Menu com as opções.
    """
    moeda1 = input('Qual sua moeda de troca? \n')
    moeda2 = input('Qual moeda você gostaria de receber?  \n')
    cotação = float(input('Digite a cotação do dia: \n'))
    valor = float(input("Qual valor você gostaria de efetuar a troca? (Digite apenas números) \n"))
    convertido = converter(valor, cotação)
    print('A conversão de ' + str(valor) + ' ' + moeda1 + ' para ' + moeda2 + ' é {:.2f}'.format(convertido))

while True:
    """
    Loop que permite adicionar mais trocas sem ter de reiniciar o programa.
    """
    menu()
    continuar = input('Deseja realizar mais alguma troca? [S/N] ')
    if continuar == 'N':
        break

print('\nMuito obrigado por utilizar nosso sistema. A Havan Exchange agradece, tenha um ótimo dia!')