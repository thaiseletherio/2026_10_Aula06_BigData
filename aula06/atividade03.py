# for i in range (5):
#     print (f'\nVenda {i+1}:')
#     compra = float(input(f'\nValor da venda: '))

#     if compra >= 200:
#         compra_desconto = compra * 0.9
#         print (f'compra com desconto. \n valor final da compra: {compra_desconto}')
#     else:
#         compra = compra * 1.0
#         print (f'compra sem desconto. \n valor final da compra: {compra}')

#correção

for venda in range (5):
    valor = float(input('\nInforme o valor da compra: '))

    if valor >= 200:
        desconto = valor * 0.10

    else:
        desconto = 0

    valor_final = valor - desconto
    print(f'Desconto de: R$ {desconto}')
    print(f'Total a pagar: R$ {valor_final}')