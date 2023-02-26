# Trabalhando com Módulos

# Importando toda a biblioteca "math".
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

# "math.ceil" arredonda para cima.
# "math.floor" arredonda para baixo.
# Pode usar também o {:.2f} para fazer o arredondamento.
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
