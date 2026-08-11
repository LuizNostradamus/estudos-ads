#Sem POO

# cor = "Preto"
# modelo = "Civic"

# def acelerar():
#     print("O carro acelerou")

# print(cor)
# print(modelo)
# acelerar()

#Com POO
# class Carro:
#     #Atributos
#     def __init__(self, cor, modelo):
#         self.cor = cor
#         self.modelo = modelo

#     #Metados
#     def acelerar(self):
#         print("O caro acelerou")

# carro1 = Carro("Preto", "Civic")

# print(carro1.cor)
# print(carro1.modelo)
# carro1.acelerar()

#Atividade
# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         self.saldo += valor
#         print("Deposito realizado")
    
#     def sacar(self, valor):
#         self.saldo -= valor
#         print("Saque realizado")

#     def mostrar_saldo(self):
#         print(f"Seu saldo atual : {self.saldo}")
#         # print("Seu saldo atual: ", self.saldo)

# conta1 = Conta("Fulano", 1000)e

# print(conta1.titular)
# conta1.depositar(500)
# conta1.sacar(200)
# conta1.mostrar_saldo()

#Atividade 2

# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco
#     def exibir_dados(self):
#         print("Nome: ", self.nome)
#         print("Preço: ", self.preco)

# mouse_game = Produto("Mouse Gamer", "R$150")
# mouse_game.exibir_dados()

#Atividade 3

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2 
        print(media)
    
    def verificar_situacao(self):
        media = (self.nota1 + self.nota2) / 2 
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

aluno = Aluno("Carlos", 8, 6)
aluno.calcular_media()
aluno.verificar_situacao()


