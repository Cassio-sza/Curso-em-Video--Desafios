#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porçao Inteira.
#Ex: Digite um numero: 6.127
    #O numero 6.127 tem a parte inteira 6.
import math
real = float(input('Digite um numero real: '))
print('O numero {} em numero inteiro fica {}'.format(real, math.trunc(real)))



