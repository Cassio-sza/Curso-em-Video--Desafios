#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

angulo = int(input('Digite o ângulo: '))
r_angulo = math.radians(angulo)
seno = math.sin(r_angulo)
cosseno = math.cos(r_angulo)
tangente = math.tan(r_angulo)
print('O angulo escolhido foi: {:.5f}.\nSeu seno é {:.5f}.\nSeu cosseno é {:.5f}\nSua tangente é {:.5f}'.format(angulo, seno, cosseno, tangente))
