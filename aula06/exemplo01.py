#entrada
valor = float(input('Valor da compra: '))

print('''
[1] - PIX (12% de desconto)
[2] - Débito (8% de desconto)
[3] - Credito (5% de desconto)
[4] - Dinheiro (15% de desconto)
''')

#operacao = True (boa prática com boleano)
desconto = 0 

opcao = int(input('Forma de pagamento: '))

match opcao:
    case 1:
        print ('--- Pix ---')
        desconto = valor * 0.12
       
    case 2:
        print ('--- Débito ---')
        desconto = valor * 0.08
        

    case 3:
        print ('--- Crédito ---')
        desconto = valor * 0.05
        

    case 4:
        print ('--- Dinheiro ---')
        desconto = valor * 0.15

    case _:
        #operacao = False
        print ('--- Opção Inválida ---')

if opcao in [1, 2, 3, 4]:
#if operacao == True:
#desconto != 0: (boa prática com 'se for diferente' - que é esse '!=')
    valor_final = valor - desconto
    print (f'\nPreço da compra: {valor:.2f}')
    print (f'Desconto: {desconto:.2f}')
    print (f'Total a pagar: {valor_final:.2f}')

else:
    print ('Por favor, escolha uma das opções acima')