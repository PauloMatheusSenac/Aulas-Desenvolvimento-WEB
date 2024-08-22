import tkinter as tk
from tkinter import messagebox


def form():
    usuario = caixa_usuario.get()
    senha = caixa_senha.get()
    conf_senha = caixa_conf_senha.get()
    
    if usuario and senha and conf_senha:
        if senha != conf_senha:
            messagebox.showwarning("Senha", "Senhas não coincidem!")
        elif usuario == senha:
            messagebox.showwarning("Erro", "Usuario e senha não podem coincidir!")
        else:
            messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
    else:
        messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")
    

    


tela = tk.Tk()
tela.title("Cadastro de Cliente")

label_usuario = tk.Label( text="Usuario:")
label_usuario.grid(row=0, column=0, padx=10, pady=10)

caixa_usuario = tk.Entry(tela)
caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

label_senha = tk.Label( text="Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=10)

caixa_senha = tk.Entry(tela)
caixa_senha.grid(row=1, column=1, padx=10, pady=10)

label_conf_senha = tk.Label( text="Confirmação de Senha:")
label_conf_senha.grid(row=2, column=0, padx=10, pady=10)

caixa_conf_senha = tk.Entry(tela)
caixa_conf_senha.grid(row=2, column=1, padx=10, pady=10)

botao_enviar = tk.Button(text="Enviar", command=form)
botao_enviar.grid(row=3, columnspan=2, pady=10)


tela.mainloop()