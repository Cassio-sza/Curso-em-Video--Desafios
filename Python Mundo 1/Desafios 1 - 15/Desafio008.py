    #Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
altura = float(input('Digite a altura em metros: '))
    #Converte o numero fornecido em cm e mm;
altura_cm = altura * 100
altura_mm = altura * 1000
print('Altura em cm: {}.\nAltura em mm: {}'.format(altura_cm, altura_mm))