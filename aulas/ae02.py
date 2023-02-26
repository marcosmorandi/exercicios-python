# Outra forma de formatar a saída do "print".
'''
um programa Python para calcular a hipotenusa de um triângulo retângulo...
com base nos comprimentos do cateto oposto e do cateto adjacente fornecidos...
pelo usuário:
'''
import math

# Leitura dos comprimentos dos catetos.
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Cálculo da hipotenusa.
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Exibição do resultado.
print(f"A hipotenusa do triângulo retângulo é {hipotenusa:.2f}")

'''
Neste programa, usamos a biblioteca math do Python...
para calcular a raiz quadrada do quadrado dos comprimentos do cateto oposto...
e do cateto adjacente.
A função input é usada para solicitar ao usuário que insira os comprimentos...
dos catetos, e a função print é usada para exibir o resultado...
com duas casas decimais.
Note que usamos o f-string para formatar a saída.
'''
