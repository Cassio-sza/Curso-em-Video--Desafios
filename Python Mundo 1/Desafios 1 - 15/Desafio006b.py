    #Primeiro peço o numero ao usuario
numero = int(input('Digite um numero: '))
    #Aqui faço as operações aritiméticas
numero_dobro = numero*2
numero_triplo = numero*3
numero_raiz = numero**(1/2)
    #Aqui usei o format apenas para facilitar na digitação, ja que as operações ja oram feitas
    #Usei \n para colocar cada sentença solicitada em uma linha;
print('O numero esolhido foi: {}.\n Seu dobro é: {}.\n Seu triplo: {}.\n Sua raiz quadrada: {:.2}'.format(numero, numero_dobro, numero_triplo, numero_raiz))
