#Inputs de preço e pagamento
preco = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Qual será a forma de pagamento? (Digite 1 para dinheiro/cheque e 2 para pagamento no cartão): '))

#Se o pagamento for em dinheiro
if pagamento == 1:
    desconto = preco / 100 * 10
    print('O valor de sua compra será de R${:.2f}, com um desconto de 10%'.format(preco-desconto))
#Se o pagamento for no cartão
elif pagamento == 2:
    #input da froma de pagamento
    forma = int(input('Digite 1 se o pagamento for à vista e 2 se for parcelado:'))
    #se o pagamento for à vista
    if forma == 1:
        desconto = preco / 100 * 5
        print('O valor de sua compra será de {:.2f}, com um desconto de 5%'.format(preco-desconto))
    #se o pagamento for parcelado
    elif forma == 2:
        parcelas = int(input('Em quantas parcelas você pretende pagar?'))
        #número das parcelas
        if parcelas == 1:
            desconto = preco / 100 * 5
            print('O valor de sua compra será de {:.2f}, com um desconto de 5%'.format(preco - desconto))
        elif parcelas == 2:
            print('O valor da sua compra será de {:.2f}, sem descontos adicionais'.format(preco))
        elif parcelas >= 3:
            juros = preco / 100 * 20
            print('O valor da sua compra será de {:.2f}, com juros de 20% sobre a compra'.format(preco + juros))
    #mensagem de erro p/forma de pagamento
    else:
        print('Por favor, digite um dos valores solicitados')
#mensagem de erro p/ pagamento
else:
    print('Por favor, digite um dos valores solicitados')



