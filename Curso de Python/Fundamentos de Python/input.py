print("===== DADOS SOBRE A ESCOLA =====")
"\n"
school_name = input("Digite o nome da escola: ")
school_adress = input("Digite o endereço da escola: ")
school_district = input("Digite o distrito onde está localizada a escola: ")
"\n"
print("===== DADOS DO ALUNO =====")
"\n"
name = input("Digite o seu nome completo: ")
adress = input("Digite o seu endereço completo: ")
nif = input("Digite o número do seu NIF com 9 dígitos: ")
"\n"
print("===== DADOS ESCOLARES =====")
"\n"
course = input("Digite o nome do seu curso: ")
number = input("Digite o seu número de aluno: ")
"\n"

print("Segue abaixo os seus de acordo com as informações fornecidas:")

print("O aluno " + name + ", com morada em " + adress + " e NIF número " + nif + ", está devidamente matriculado no curso de " + course + ", sob o número " + number + ", na escola " + school_name + ", situada a " + school_adress + ", em " + school_district + "." )

print("O aluno {}, com morada em {} e NIF número {}, está devidamente matriculado no curso de {}, sob o número {}, na escola {}, situada a {}, em {}.".format(name, adress, nif, course, number, school_name, school_adress, school_district))