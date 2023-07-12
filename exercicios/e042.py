'''
Exercício 042 - Feito
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
- Equilátero: Todos os lado iguais
- Isósceles: Dois lados iguas
- Escaleno: Todos os lados diferentes
'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='') # Aqui o "end" esta juntando o "print" abaixo na mesma linha, sem dar "enter".
    if r1 == r2 == r3: # Se o r1 for igual a r2 e r2 igual a r3, r3 só pode ser igual a r1 também. Nesse caso o "==" equivale ao "and", só que de forma simplificada.
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: # Nesse caso a lógica acima não funciona, tem que comparar todas as possibilidades, r1 sendo diferente de r2, não significa que o r3 sendo diferente de r2 será também diferente de r1, r3 e r1 podem ser iguais. Tem que comparar a diferença de r3 com r1.
        print('ESCALENO!')
    else: # Se for triângulo, mas não equilátero nem escaleno, só pode ser isósceles.
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
