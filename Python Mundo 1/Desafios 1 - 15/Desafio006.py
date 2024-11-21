    #Primeiro vou criar o input do numero que o usuario vai digitar
numero = int(input('Digite um número: '))
    #Vou imprimir o resultado colocando uma resposta em cada linha, usando o \n
    #Preferi fazer as operações aritimeticas direto na função .format
print('Voce escolheu o numero {}. \n O dobro dele é {}.\n O triplo dele é {}.\n E sua raiz quadrada é {}.'.format(numero, numero*2, numero*3, numero**(1/2)))