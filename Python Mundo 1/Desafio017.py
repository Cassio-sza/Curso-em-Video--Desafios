#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retaangulo, calcule e mostre o comprimento da hipotenusa.

'''import math

c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(c_oposto**2 + c_adjacente**2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(co, ca)

print('A hipotenusa vai medir {:.2}'.format(hipotenusa))

