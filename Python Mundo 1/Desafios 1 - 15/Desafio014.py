#Escreva um programa que conerta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = celsius * 1.8 + 32
print('Temperatura em F°: {:.2f}'.format(fahrenheit))
