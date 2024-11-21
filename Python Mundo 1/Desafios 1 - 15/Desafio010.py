#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#Considere o dollar a R$3,27
dinheiro = float(input('Digite o valor em dinheiro: '))
dollar = 3.27
print('dinheiro: R$ {:.2f} \nDolar: R$ {:.2f}'.format(dinheiro, dinheiro/dollar))
