'''
Exercício 044 - Feito
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS GUANABARA ')) # "{:^40}" significa centralizado em 40 espaços. "{:=^40}" assim preence o centralizado com o simbolo de "=".

preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total  / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} COM JUROS.')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
