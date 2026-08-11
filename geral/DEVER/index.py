
#Atividade 1
# nomes = []

# for i in range(5):
#     n1 = input("Digite os nomes: ")
#     nomes.append(n1)

# print(nomes)

#Atividade 2

# frutas = ["maçã", "banana", "uva", "laranja"] 

# n = input("Remova a sua fruta: ")
# if n == "maçã":
#     frutas.remove("maçã")
# elif n == "banana":
#     frutas.remove("banana")
# elif n == "uva":
#     frutas.delete("uva")
# elif n == "laranja":
#     frutas.delete("laranja")

# n1 = input("Adicione sua fruta: ")
# frutas.append(n1)

# print(frutas)

#Atividade 3

# n = []
# a = 0
# for i in range(5):
#     n1 = int(input("Digite seu numero: "))
#     n.append(n1)
#     a = a + n1 
# print(n)
# print("Resultado final: ", a)

#Atividade 4

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(10):
#     if numeros %2 == 0:
#         print("numeros pares: ", numeros)

#Atividade 5

# notas = []
# a = 0

# for i in range(4):
#     suas_notas = float(input("Coloque suas notas: "))
#     notas.append(suas_notas)
#     a = a + suas_notas / 2
#     if a >= 7:
#         print("Aprovado")
#     else:
#         print("Reprovado")

#Atividade 5 - Professor

# notas = []
# a = 0

# for i in range(4):
#     suas_notas = float(input("Coloque suas notas: "))
#     notas.append(suas_notas)

# for suas_notas in notas:
#     a = a + suas_notas
# media = a / len(notas)
# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

#Atividade 6

# nome = ["Luiz", "Gabriel", "Kaun", "Henry"]

# n = input("Digite seu nome: ")

# if n in nome:
#     print("Aluno encontrado")
# else:
#     print("Aluno não encontrado")

#Atividade 7

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("Quantidade", len(numeros))
# print("Quantidade", max(numeros))
# print("Quantidade", min(numeros))

#Atividade 8

# tarefas = []

# for i in range(3):
#     add_taf = input("Adicione suas tarefas: ")
#     tarefas.append(add_taf)
# print("Tarefas: ", tarefas)

# rem_taf = input("Remove sua tarefa: ")
# tarefas.remove(rem_taf)
# print("Tarefas: ", tarefas)
   
