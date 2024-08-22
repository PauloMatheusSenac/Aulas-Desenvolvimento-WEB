import tkinter as tk
from tkinter import messagebox

def menu(usuario):
    tela_menu = tk.Tk()
    tela_menu.title("Menu")
    tela_menu.config(width=800,height=800,)
    
    menu = tk.Label(tela_menu, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial",50))
    menu.grid(row=0, column=0, padx=400, pady=400)
    botao_enviar = tk.Button(text="Enviar", command=form)
    botao_enviar.grid(row=3, columnspan=2, pady=10)
    botao_enviar = tk.Button(text="Enviar", command=form)
    botao_enviar.grid(row=3, columnspan=2, pady=10)
    botao_enviar = tk.Button(text="Enviar", command=form)
    botao_enviar.grid(row=3, columnspan=2, pady=10)
    botao_enviar = tk.Button(text="Enviar", command=form)
    botao_enviar.grid(row=3, columnspan=2, pady=10)



    tela.mainloop()




def form():
    usuario = caixa_usuario.get()
    senha = caixa_senha.get()
    conf_senha = caixa_conf_senha.get()

    logins.append(usuario)
    senhas.append(senha)

    
    if usuario and senha and conf_senha:
        if senha != conf_senha:
            messagebox.showwarning("Senha", "Senhas não coincidem!")
        elif usuario == senha:
            messagebox.showwarning("Erro", "Usuario e senha não podem coincidir!")
        else:
            messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
            pedido = messagebox.askyesno("Pedido", message="Deseja fazer seu pedido?")
            if pedido:
                logar(usuario)
            else:
                quit()

    else:
        messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")
    
def logar():
    usuario = caixa_usuario.get()
    senha = caixa_senha.get()

    if usuario and senha:
        if usuario in logins:
            if senha in senhas:
                messagebox.showwarning("Cadastro encontrado", f"Olá {usuario}, Seja Bem Vindo, \nvocê sera direcionado ao menu agora!!!!")
                menu()
                print("teste")
            else:
                messagebox.showwarning("Senha", "Senha Incorreta")
        else:
            messagebox.showwarning("Não encontrado", "Usuario não cadastrado!")
    else:
        messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")


                
escolha = messagebox.askyesno(title="Logar ou Cadastrar", message="Voce ja tem cadastro em nosso sistema?")

logins = ["admin"]
senhas = ["123","125"]
if escolha:
    tela = tk.Tk()
    tela.title("Login")
    tela.config(width=80,height=80)

    label_usuario = tk.Label( text="Usuario:")
    label_usuario.grid(row=0, column=0, padx=10, pady=10)

    caixa_usuario = tk.Entry(tela)
    caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

    label_senha = tk.Label( text="Senha:")
    label_senha.grid(row=1, column=0, padx=10, pady=10)
    
    caixa_senha = tk.Entry(tela)
    caixa_senha.grid(row=1, column=1, padx=10, pady=10)
    
    botao_logar = tk.Button(text="     Login     ", command=logar)
    botao_logar.grid(row=3, column=1, pady=20, padx=50, )


    tela.mainloop()
else:
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



    botao_logar = tk.Button(text="Login", command=logar)
    botao_logar.grid(row=3, column=1, pady=10)
    botao_cadastrar = tk.Button(text="Cadastrar", command=form)
    botao_cadastrar.grid(row=3, column=0)


    tela.mainloop()