    #faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%.
preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o desconto: '))
novo_preco = preco * desconto / 100
print('O valor com desconto fica: R${}'.format(preco - novo_preco))