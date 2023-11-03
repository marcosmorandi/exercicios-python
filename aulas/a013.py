# Estrutra de repetição "for".

for c in range(0, 6): # Começando com "1" não considera o ultimo número, para no 5. Então começe no "0".
    print('Oi')
print('FIM')

for c in range(1, 6):
    print(c)
print('FIM')

for c in range(5, 0, -1): # Aqui esta pedindo uma contagem regressiva, de menos 1 em 1.
    print(c)
print('FIM')

for c in range(10, 0, -2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(1, n+1): # Sem o "+1" ele não exibe o número, pois para no número digitado e não exibe.
    print(c)
print('FIM')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n # No Python pode ser representado por "s += n"
print(f'O somatório de todos os valores foi {s}')

#    "if pessoa == 1 and sexo in 'Mm':" Nesse caso o "in" compara "M" e "m", maiúsculo e minúsculo.
