nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é mais bonito que Gustavo!')
print(f'Bom dia {(nome)}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {(m):.1f}.')
'''
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
'''
# Condição simplificada:
print('Parabéns!' if m >= 6 else 'Estude Mais!')
