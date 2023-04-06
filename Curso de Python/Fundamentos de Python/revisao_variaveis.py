print("EXERCÍCIO 01")

idade = 47      
metade_idade = idade / 2
saudacao = "Olá"
despedida = "Adeus,"
nome = "Marcos"
despedida_com_nome = despedida + " " + nome

print(idade)
print(metade_idade)
print(saudacao)
print(despedida)
print(despedida_com_nome)

print("===============================================================")

print("EXERCÍCIO 02")

descricao_pc = "Notebook Dell"
preco_pc = 1000
rato = "Rato Samsung"
preco_rato = 20
teclado = "Teclado Wireless"
preco_teclado = 100
iva = 1.23
total_sem_IVA = preco_pc + preco_rato + preco_teclado
total_com_IVA = (preco_pc + preco_rato + preco_teclado) * iva


print("Você comprou: 01 " +  descricao_pc + ", 01 " + rato + " e 01 " + teclado + ". O total da sua compra foi de " + str(total_sem_IVA) + " euros, sem os impostos. O total da sua compra com impostos foi de " + str(total_com_IVA) + " euros.")

print("Você comprou: 01 {}, 01 {} e 01 {}. O total da sua compra foi de {:.2f} euros, sem os impostos. O total da sua compra com impostos foi de {:.2f} euros.".format(descricao_pc, rato, teclado, total_sem_IVA, total_com_IVA))