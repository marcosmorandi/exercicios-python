'''
O comando "print" exibe algo na tela, equivale a dizer "escreva".
'''
print('\nHello word!') # Aspas simples, escreve mensagem.
print(7+4) # Sem aspas, faz o cálculo.
print('7'+'4') # Se quiser juntar mensagens, coloque o "+" entre elas.
print('Hello', 5) # Tem horas que o "+" funciona melhor, tem horas que a "," funcionas melhor.

'''
Variáveis:
Começe sempre com letra minúscula.
O "=" se lê "recebe".
Exibindo variáveis já definidas
'''
print('') # "print" vazio para espaço para entre linhas. Pode se usar o "\n" no fim do "print" anterior ou no começo do próximo, dispensado essa linha com o comando vazio.
nome = 'Jon'
idade = '25 anos'
peso = '70.5 kilos'
print(nome + ', ' + idade + ', ' + peso + '.')

'''
O comando "input" escreve e recebe dados digitados pelo usuário. equivale a dizer "escreva e leia".
'''
print('')
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')
print(nome + ', ' + idade + ' anos, ' + peso + ' kilos.')
