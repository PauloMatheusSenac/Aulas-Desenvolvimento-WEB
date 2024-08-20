import tkinter as tk
from tkinter import messagebox

# def contar_cliques():
#     global contador
#     contador += 1
#     janela.config(text=f'Cliques: {contador}')
#     if contador > 10:
#         contador = 0

# def contarimp():
#     global cont
#     cont += 1
#     erros = 0
#     print(f'O Botão foi clicado {cont} vezes')
#     if cont == 10:
#         print("Parabéns, você clicou 10 vezes")
#         print(20 * "*")
#         print(20 * "*")
#         print(20 * "*")
#         print(20 * "*")
#     elif cont > 10:
#         messagebox.showwarning(title="Clicou +10", message="Você clicou mais de 10 vezes!")
#         aceita = messagebox.askyesno(title="Assumindo a Culpa", message="Vc entende que clicou a mais ne?")
#         if aceita :
#             messagebox.showwarning(title="Aceitou", message="Vou resetar, na proxima vez le o que ta escrito po!!!!!")
#             cont = 0
#             #erros +=1
#             #print(erros)
        
#         else:
#             messagebox.showerror(title="Não aceitou", message="Basta Ler parça")
#             sair()
#     #if erros == 2:
#         #messagebox.showerror(title="Não aceitou", message="Basta Ler parça")
#         #sair()    
            

# def clicou():
#     contar_cliques()
#     contarimp()

# def sair():
#     print("OVO SAIRRRRR")
#     tela.quit()


    

# ############################################################################################
# tela = tk.Tk()
# tela.title("Contador de Cliques")

# contador = 0
# cont = 0

# botao = tk.Button(tela, text="Clique até no máximo 10 vezes", command=clicou, width=50, height=10)
# botao.pack(pady=20)

# janela = tk.Label(tela, text=f'Cliques: {contador}', font=("Arial", 12))
# janela.pack(pady=20)

# tela.mainloop()
####################################################################################################################################################################################################################################################################################
# def form():
#     usuario = caixa_usuario.get()
#     senha = caixa_senha.get()
#     conf_senha = caixa_conf_senha.get()
    
#     if usuario and senha and conf_senha:
#         if senha != conf_senha:
#             messagebox.showwarning("Senha", "Senhas não coincidem!")
#         elif usuario == senha:
#             messagebox.showwarning("Erro", "Usuario e senha não podem coincidir!")
#         else:
#             messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
#     else:
#         messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos de cadastro e tente novamente!")
    

    


# tela = tk.Tk()
# tela.title("Cadastro de Cliente")

# label_usuario = tk.Label( text="Usuario:")
# label_usuario.grid(row=0, column=0, padx=10, pady=10)

# caixa_usuario = tk.Entry(tela)
# caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

# label_senha = tk.Label( text="Senha:")
# label_senha.grid(row=1, column=0, padx=10, pady=10)

# caixa_senha = tk.Entry(tela)
# caixa_senha.grid(row=1, column=1, padx=10, pady=10)

# label_conf_senha = tk.Label( text="Confirmação de Senha:")
# label_conf_senha.grid(row=2, column=0, padx=10, pady=10)

# caixa_conf_senha = tk.Entry(tela)
# caixa_conf_senha.grid(row=2, column=1, padx=10, pady=10)

# botao_enviar = tk.Button(text="Enviar", command=form)
# botao_enviar.grid(row=3, columnspan=2, pady=10)


# tela.mainloop()

####################################################################################################################################################################################################################################################################################

def trocaazul():
    print("trocou para azul")
    tela.config(bg="blue")

def trocaverde():
    print("trocou para verde")
    tela.config(bg="green")

def trocavermelho():
    print("trocou para vermelho")
    tela.config(bg="red")


tela = tk.Tk()
tela.title("Trocando cores")


botao1 = tk.Button(tela, command=trocaazul, text="Trocar para Azul", fg='blue')
botao1.grid(pady=10, padx=10)

botao2 = tk.Button(tela, command=trocaverde, text="Trocar para Verde", fg='green')
botao2.grid(pady=10, padx=10)

botao3 = tk.Button(tela, command=trocavermelho, text="Trocar para Vermelho", fg='red')
botao3.grid(pady=10, padx=10)


tela.mainloop()



