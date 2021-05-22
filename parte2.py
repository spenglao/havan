def menu():
    """
    Definição de menu de opções que aparecerá após o registro do cliente.
    """
    print('Qual dado você deseja solicitar? ')
    print('')
    print('[1] Lista de operações')
    print('[2] Valor total das operações')
    print('[3] Valor total das taxas cobradas')
    print('[4] Filtrar operações por data e/ou cliente')
    print('[0] Não desejo nenhum dado, encerrar')

"""
Definição de variáveis.
"""
clientela = list()
cliente = dict()
valor_totalusd = soma = 0
valor_totalbrl = soma = 0

print('Bem vindo ao Havan Exchange! \nPor favor digite os dados de cada cliente, lembrando que trabalhamos apenas com conversões BRL/USD e nossa taxa de serviço é 10%.')

while True:
    """
    Loop que fará o registro de cada cliente.
    """
    cliente.clear()
    cliente['nome'] = str(input('Nome: '))
    cliente['moeda_origem'] = str(input('Moeda de origem (Escolha entre BRL/USD): '))
    if cliente['moeda_origem'] == 'BRL':
        cliente['moeda_destino'] = str('USD')
    elif cliente['moeda_origem'] == 'USD':
        cliente['moeda_destino'] = str('BRL')
    cliente['data_operação'] = str(input('Data da operação: (DDMMYYYY) '))
    cliente['valor_original'] = float(input('Valor de câmbio: '))
    cliente['taxa_dia'] = float(input('Taxa do dia: '))
    if cliente['moeda_origem'] == 'BRL':
        cliente['valor_convertido'] = float(cliente['valor_original']/cliente['taxa_dia']*0.9)
        valor_totalbrl += cliente['valor_original']
    elif cliente['moeda_origem'] == 'USD':
        cliente['valor_convertido'] = float(cliente['valor_original']*cliente['taxa_dia']*0.9)
        valor_totalusd += cliente['valor_original']
    cliente['taxa_cobrada'] = float(valor_totalusd*cliente['taxa_dia']*0.1+valor_totalbrl*0.1)
    clientela.append(cliente.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp == 'N':
        break

while True:
    menu()
    """
    Loop que dará as opções de diferentes solicitações de acordo com os clientes registados.
    """
    opção = int(input('Digite o número de sua solicitação: '))

    if opção == 1:
        pass
    elif opção == 2:
        print(f'O valor total das operações de BRL é {valor_totalbrl}')
        print(f'O valor total das operações de USD é {valor_totalusd}')
    elif opção == 3:
        pass
    elif opção == 4:
        pass
    elif opção == 0:
        break

    resp2 = input('Deseja solicitar mais algum dado? [S/N]')
    if resp2 == "N":
        break
        
print('Muito obrigado por utilizar nossos serviços, até uma próxima!')


