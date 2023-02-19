'''
Exercicio 008 - Feito
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
'''

medida_metros = float(input('Uma distância em metros: '))
km = medida_metros / 1000 # km: quilômetros
hm = medida_metros / 100 # hm: hectómetro
dam = medida_metros / 10 # dam: decâmetro
dm = medida_metros * 10 # dm: decímetros
cm = medida_metros * 100 # cm: centímetros
mm = medida_metros * 1000 # mm: milímetros

print('A medida de {}m corresponde a: '.format(medida_metros)) # m: metros
print('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))
