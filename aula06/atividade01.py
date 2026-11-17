#entrada
valor = float(input('Valor do ingresso: '))
desconto = 0

print ('''
[1] - Inteira (sem desconto)
[2] - Meia entrada (50% de desconto)
[3] - Promoção (30% de desconto)
''')

opcao = int(input('Escolha Tipo de Entrada: '))

match opcao:
    case 1: 
        print ('---Inteira---')
      
    case 2:
        print ('---Meia Entrada---')
        desconto = valor * 0.5
    case 3: 
        print ('---Promoção---')
        desconto = valor * 0.3
    case _:
        print ('Opção Inválida. Escolha uma opção acima.')

if opcao in [1, 2, 3]:
    valor_final = valor - desconto
    print (f'Valor da compra: R$ {valor_final}')

else:
    print ('Digite uma das opções acima')
#correção igual a essa resolução

