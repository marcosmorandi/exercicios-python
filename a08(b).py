# Trabalhando com Módulos

# Importando somente o "sqrt" da biblioteca "math".
from math import sqrt, floor # Pode importar mais de uma função, basta separar por virgula. Ex: "from math import sqrt, floor"
num = int(input('Digite um número: '))
raiz = sqrt(num) # Não precisa utilizar a referência "math", usa direto a função "sqrt".

print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
