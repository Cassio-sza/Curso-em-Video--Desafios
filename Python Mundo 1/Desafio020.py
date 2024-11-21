#O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Primeiro ou importar o modulo random e fazer os inputs dos nomes:

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

#Colocar os nomes numa lista e sortear a ordem usando o shuffle

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

#Gerar o output

print('A ordem de apresentação é:', alunos)      

