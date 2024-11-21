#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua area e a quantidade  de tinta necessaria para pinta-
# Sabemos que cada litro de tinta pinta uma area de 2m^2
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
print('Sua parede tem {} m². \nPara pintar, usaremos {} litros de tinta.'.format(altura*largura,(altura*largura)/2))