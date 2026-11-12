#entrada
valor = float(input('Valor do ingresso: '))

print ('''
[1] - Inteira (sem desconto)
[2] - Meia entrada (50% de desconto)
[3] - Promoção (30% de desconto)
''')

opcao = int(input('Escolha Tipo de Entrada: '))

match opcao:
    case 1: 
        print ('---Inteira---')
        valor = valor * 1.0
    case 2:
        print ('---Meia Entrada---')
        valor = valor * 0.5
    case 3: 
        print ('---Promoção---')
        valor = valor * 0.7
    case _:
        print ('Opção Inválida. Escolha uma opção acima.')

if opcao in [1, 2, 3]:
    print (f'Valor da compra: R$ {valor}')
