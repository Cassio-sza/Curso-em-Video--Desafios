teclado = input('Digite algo no telado: ')
print(type(teclado))
print('E um valor numérico?', teclado.isnumeric())
print('É um valor decimal?', teclado.isdecimal())
print('E um valor alfadecimal?', teclado.isalnum())