#Escreva um programa que pergunte a qquantidade de Km rodado por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Kms rodados? :'))
dias = float(input('Quantos dias com o carro? :'))
preco = dias * 60 + km * 0.15
print('Total a pagar: R${:.2f}'.format(preco))


