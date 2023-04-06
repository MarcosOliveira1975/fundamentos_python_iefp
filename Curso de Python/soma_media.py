number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))
number3 = float(input('Digite o terceiro número: '))

soma = (number1 + number2 + number3)
media = (number1 + number2 + number3) / 3

print('A soma dos números digitados é: ', soma,'. E a média dos três números é: ', media,'.')

if media >= 7:
    print("De acordo com sua média você está APROVADO!")
else: 
    print("De acordo com sua média você está REPROVADO!")

x = int(input('Digite um número para descobrir se ele é positivo ou negativo: '))

if x > 0:
    print('O número que você digitou foi o', x, 'e ele é POSITIVO!')
else:
    print('O número que você digitou foi o', x, 'e ele é NEGATIVO!')

    #pesquisar como imprimir um número negativo em Python