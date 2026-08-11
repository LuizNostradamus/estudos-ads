from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

#janela

janela = Tk()
janela.title("Cadastro do Paciente")
janela.geometry("900x600")

#notebook (abas)

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

#aba1 - cadastro

aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")


#aba2 - tabelas

aba2 = Frame(abas)
abas.add(aba2, text="Pacientes cadastrados")

#Função Cadastra
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    data = entry_data.get()
    email = entry_email.get()
    sus = entry_sus.get()
    telefone = entry_telefone.get()
    contato = entry_contato.get()
    if nome == "" or telefone == "" or email == "" or cpf == "" or data == "" or sus == "" or contato == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
    else:
        tabela.insert("", END, values=(nome, telefone, email, cpf, data, sus, contato))
        entry_nome.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_contato.delete(0, END)
        entry_cpf.delete(0, END)
        entry_sus.delete(0, END)
        entry_data.delete(0, END)

        messagebox.showinfo("Sucesso", "Paciente Cadastrado")

##aba cadastro
Label(aba1, text="Nome completo").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF").pack(pady=5)
entry_cpf = Entry(aba1, width=40)
entry_cpf.pack()

Label(aba1, text="Data de nascimento").pack(pady=5)
entry_data = Entry(aba1, width=40)
entry_data.pack()

Label(aba1, text="Email").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Convenio/SUS").pack(pady=5)
entry_sus = Entry(aba1, width=40)
entry_sus.pack()

Label(aba1, text="Telefone").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Contato de emergência").pack(pady=5)
entry_contato = Entry(aba1, width=40)
entry_contato.pack()

Button(
    aba1, 
    text="Cadastrar",
    bg="green",
    fg="white",
    width=20,    
    command=cadastrar 
).pack(pady=20)

##aba tabela 

colunas = ("Nome completo", "CPF", "Data de nasimento", "Telefone", "Email", "Convenio/SUS", "Contato de emergencia")
tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show= "headings",
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill="both", expand=True, pady=20)




janela.mainloop()