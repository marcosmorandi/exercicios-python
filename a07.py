'''
Operações Aritméticas:
+ adição
- subtração
* multiplicação
/ divisão
** potência ou exponenciação
// divisão inteira, sem a "," ou "."
% resto da divisão ou módulo
5+2==7, "=" duas vezes para "igual", somente um "=" significa "recebe".
5-2==3
5*2==10
5/2==2.5
5**2==25
5//2==2
5%2==1
'oi'+'olá'==oiolá
'oi'*5==oioioioioi
print('-'*20)==--------------------

Ordem de Precedência:
1º ()
2º **
3º *, /, //, %, se tiver todos esses faz na ordem, primeiro o que aparecer primeiro.
4º +, -, também por ordem.
Sempre cuide da ordem de precedência, senão ao executar um programa ele pode funcinar, mas dar um resultado errado.
5+3*2==11, não 16
3*5+4**2==31, não 361
3*(5+4)**2==243, os "()" fizeram a soma ficar em 1º na ordem de precedência.

Limpar o terminal no Python para Windows:
import os
clear = lambda: os.system('cls')
clear()
'''

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome)) # "{}" é uma máscara de substituição. Nesse exemplo está colocando o "nome" em 20 espaços(20), centralizado(^), com o igual ao redor(=).

print('')

n1 = int(input('Uma valor: '))
n2 = int(input('Outro valor: ')) # Sempre que possível digite para internalizar o conhecimento, nunca copie e cole código.
print('A soma vale {}'.format(n1+n2)) # Nesse caso é desnecessário armazenar em variável pois não será usado novamente.

print('')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d)) # Pode colocar valores nas máscaras, {0}{1}{2} para se organizar, ou {2}{1}{0} para mudar ordem...
print('Divisão inteira {} e potência {}'.format(di, e)) # ...mas não é obrigatório, por padrão ele segue a sequencia crescente.

print('')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # Nesse caso o "end=' '" serve para não quebrar linha de um print para outro...
print('Divisão inteira {} e potência {}'.format(di, e)) # ... pode se adicionar um simbolo no espaço vazio, como o ">>>" por exemplo.

print('')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}\no produto é {}\ne a divisão é {:.3f}'.format(s, m, d)) # Nesse caso o "\n" serve para quebrar a linha no meio do print.
print('Divisão inteira {}\ne potência {}'.format(di, e))
