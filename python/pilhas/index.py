import tkinter as tk
from tkinter import messagebox

# Pilha que armazenará informações
pilha_undo= []
# Pilha que armazerá e utilizará para refazer
pilha_redo= []

def adicionar ():
    texto = entrada.get()
    if texto == "":
        messagebox.showwarning(
            "aviso",
            "Digite alguma coisa"
        )
        return
    # push
    pilha_undo.append(texto)
    pilha_redo.clear()
    atualizar_historico()

    entrada.delete(0,tk.END)

def atualizar_historico():
    lista.delete(0,tk.END)

    for item in pilha_undo:
        lista.insert(tk.END, item)

janela = tk.Tk()
janela.title("Projeto pilha - undo e redo")
janela.geometry("500x400")

entrada= tk.Entry(janela, width=50)
entrada.pack(pady=20)

butao_adicionar= tk.Button(janela, text="Adicionar", command=adicionar)
butao_adicionar.pack()

# Butão desfazer
butao_undo= tk.Button(janela, text="Desfazer")
butao_undo.pack(pady=5)

# Butão refazer
butao_redo = tk.Button(janela, text="Refazer")
butao_redo.pack(pady=5)

lista= tk.Listbox(janela, width=50, height=10)
lista.pack(pady=20)

janela.mainloop()

