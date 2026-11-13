for i in range (5):
    print (f'\nVenda {i+1}:')
    compra = float(input(f'\nValor da venda: '))

    if compra >= 200:
        compra_desconto = compra * 0.9
        print (f'compra com desconto. \n valor final da compra: {compra_desconto}')
    else:
        compra = compra * 1.0
        print (f'compra sem desconto. \n valor final da compra: {compra}')