import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.rowconfigure(0, weight = 1)
janela.columnconfigure([0,1],weight = 1)
janela.title("Faça o seu login aqui:")
def login():
    usuario1 = 'Usuario'
    senha1 = '1234'
    if usuario.get()==usuario1 and senha.get()==senha1:
        messagebox.showinfo(title='login', message = 'Login efetuado com sucesso')
    else:
       messagebox.showinfo(title='login', message = 'Login ou senha invalida')

mensagem1 = tk.Label(text = "Entre com o seu usuário e senha:", fg = "white", bg = "black", width =40, height = 1)
mensagem1.grid(row = 0, column = 0, columnspan = 2, sticky = "NSWE")
mensagem2 = tk.Label(text = "Login", height = 2)
mensagem2.grid(row = 1, column = 0)
mensagem3 = tk.Label(text = "Senha", height = 2)
mensagem3.grid(row = 3, column = 0)
usuario = tk.Entry()
usuario.grid(row = 1, column = 1)
senha = tk.Entry(janela, show= '*')

senha.grid( row = 3, column = 1)


botao = tk.Button(text = "Acesse",command = login, height = 1, width = 5)
botao.grid(row = 5, column = 1)


janela.mainloop()





