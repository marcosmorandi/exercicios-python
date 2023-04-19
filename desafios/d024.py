'''
Desafio 024 - Feito
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip().split() # ".strip" remove espaços vazios antes e depois da string, ".split" divide a string onde tem espaços no meio, com nova indexação 0,1,2...

# Sempre tente antecipar qualquer possível erro do usuário e corrigir.
if (cidade[0].lower()) == 'santo': # Independente de como o usuário digitar(minúscula, maiúscula, misturado), ele joga para minúscula e verifica a palavra na posição "0" da string.
    print('Esta cidade começa com o nome "Santo".')
else:
    print('Esta cidade não começa como nome "Santo".')
