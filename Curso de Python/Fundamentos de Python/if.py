mes = input('Digite o mês que deseja fazer o cálculo: ')
receita = float(input('Digite o valor da receita: '))
despesa = float(input('Digite o valor da despesa: '))
resultado = receita - despesa

print('O resultado do mês de {} foi de {:.2f} euros'.format(mes, resultado))

if resultado < 0:
    print('O resultado do mês de {} foi NEGATIVO.'.format(mes))
elif resultado > 0:
    print('O resultado do mês de {} foi POSITIVO!'.format(mes))
else:
    print('O resultado do mês de {} não deu lucro, nem prejuízo.'.format(mes))
