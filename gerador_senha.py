import random

count = 0

print('GERADOR DE SENHAS')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*@%$&-.+?!'

quant_senhas = int(input('\nQuantidade de senhas a serem geradas: '))

tamanho_senhas = int(input('Quantidade de caracteres nas senhas (tamanho das senhas): '))

print('\nSenhas Geradas:')

for senha in range(quant_senhas):
    count += 1
    senhas = ''
    for x in range(tamanho_senhas):
        senhas += random.choice(caracteres)
    print(f'|   Senha {count}: {senhas}   |')
