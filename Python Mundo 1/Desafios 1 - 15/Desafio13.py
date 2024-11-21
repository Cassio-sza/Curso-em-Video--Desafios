#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
salario = float(input('Digite o salário do funcionário: '))
aumento = salario + (salario * 15 / 100)
print('O salário do funcionario será reajustado para: \n{:.2f}'.format(aumento))