name = input("Digite oseu primeiro nome: ")
surname = input("Digite o seu sobrenome: ")
adress = input("Digite o nome da cidade onde mora: ")
age = int(input("Digite a sua idade: "))
heightEmCentimetros = float(input('Digite a sua altura em centímetros: '))

heightEmMetros = heightEmCentimetros / 100

text = 'Olá, meu nome é ' + name + ' ' + surname + ', moro em ' + adress + ', tenho ' + str(age) + ' anos de idade e minha altura é ' + str(heightEmMetros) + 'm.'

print(text)

print ('Olá, meu nome {} {}, moro em {}, tenho {} anos de idade e minha altura é {:.2f}m'.format(name, surname, adress, str(age), heightEmMetros))