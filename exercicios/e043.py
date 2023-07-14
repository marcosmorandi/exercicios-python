'''
Exercício 043 - Feito
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25: # Isso equivale "imc maior igual a 18.5 e menor que 25", lendo do meio, da variavél "imc". Não do começo, da esquerda para a direita.
    print('PARABÉNS, você está na faixa de PESO NORAML.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
