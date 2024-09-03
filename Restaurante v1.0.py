import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



class Sistema:
    def __init__(self):
        self.logins = {"admin": "123"}
        self.pedidos = []
        self.inicio()

    def inicio(self):
        self.inicial = tk.Tk()
        self.inicial.title("Escolha")
        self.inicial.geometry("1x1")
        escolha = messagebox.askyesno(title="Logar ou Cadastrar", message="Você já tem cadastro em nosso sistema?")
        self.inicial.destroy()
        self.window = tk.Tk()
        self.window.title("Login")

        if escolha:
            self.login()
        else:
            self.cadastrar()

        self.window.mainloop()

    def login(self):
        tk.Label(self.window, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.caixa_usuario = tk.Entry(self.window)
        self.caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.caixa_senha = tk.Entry(self.window, show='*')
        self.caixa_senha.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.window, text="Login", command=self.logar).grid(row=2, column=1, pady=20, padx=50)

    def cadastrar(self):
        tk.Label(self.window, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.caixa_usuario = tk.Entry(self.window)
        self.caixa_usuario.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        tk.Label(self.window, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.caixa_senha = tk.Entry(self.window, show='*')
        self.caixa_senha.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        tk.Label(self.window, text="Confirmação de Senha:").grid(row=2, column=0, padx=10, pady=10)
        self.caixa_conf_senha = tk.Entry(self.window, show='*')
        self.caixa_conf_senha.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        tk.Button(self.window, text="Cadastrar", command=self.incluir).grid(row=3, column=1, pady=20, padx=20)

    def logar(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()
        
        

        if usuario and senha:
            if usuario in self.logins:
                if senha == self.logins[usuario]:
                    messagebox.showinfo("Login bem-sucedido", f"Olá {usuario}, Seja Bem Vindo!")
                    self.window.destroy()
                    self.menu(usuario)
                    
                    
                else:
                    messagebox.showwarning("Senha", "Senha Incorreta")
            else:
                messagebox.showwarning("Não encontrado", "Usuário não cadastrado!")
        else:
            messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos e tente novamente!")

    def incluir(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()
        conf_senha = self.caixa_conf_senha.get()
        
        

        if usuario and senha and conf_senha:
            if senha != conf_senha:
                messagebox.showwarning("Senha", "Senhas não coincidem!")
            elif usuario == senha:
                messagebox.showwarning("Erro", "Usuário e senha não podem coincidir!")
            else:
                self.logins[usuario] = senha
                messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
                pedido = messagebox.askyesno("Pedido", "Deseja fazer seu pedido?")
                if pedido:
                    self.window.destroy()
                    self.menu(usuario)
                    
                    
                else:
                    self.window.destroy()
        else:
            messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos e tente novamente!")

    def menu(self, usuario):
        self.menu_window = tk.Tk()
        self.menu_window.title("Menu")
        self.menu_window.geometry("400x800")
        self.menu_window.config(bg="#CC0000")
        
        

        menu_label = tk.Label(self.menu_window, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20), bg="#FF9933")
        menu_label.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

        tk_principal = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png").subsample(5, 5)
        tk_bebidas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png").subsample(5, 5)
        tk_alcoolicas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png").subsample(5, 5)
        tk_sobremesas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png").subsample(5, 5)
        tk_menu_chef = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png").subsample(5, 5)
        tk_entradas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png").subsample(5, 5)
        tk_pedidos = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pedir.png").subsample(5, 5)

        botao_entradas = tk.Button(self.menu_window, image=tk_entradas, command=lambda: self.categorias("entradas"), bg="#FF9933")
        botao_entradas.grid(row=1, column=0, pady=20, padx=50, sticky="nw") 
        desc_entradas = tk.Label(self.menu_window, text="ENTRADAS", font=("Arial", 10), bg="#FF9933")
        desc_entradas.grid(row=2, column=0, sticky="nw", padx=65)

        botao_principal = tk.Button(self.menu_window, image=tk_principal, command=lambda: self.categorias("pratos"), bg="#FF9933")
        botao_principal.grid(row=3, column=0, pady=20, padx=50, sticky="nw")
        desc_principal = tk.Label(self.menu_window, text="PRATOS PRINCIPAIS", font=("Arial", 10), bg="#FF9933")
        desc_principal.grid(row=4, column=0, sticky="nw", padx=40)

        botao_bebidas = tk.Button(self.menu_window, image=tk_bebidas, command=lambda: self.categorias("bebidas"),bg="#FF9933")
        botao_bebidas.grid(row=5, column=0, pady=20, padx=50, sticky="nw")
        desc_bebidas = tk.Label(self.menu_window, text="BEBIDAS", font=("Arial", 10), bg="#FF9933")
        desc_bebidas.grid(row=6, column=0, sticky="nw", padx=65)

        botao_alcoolicas = tk.Button(self.menu_window, image=tk_alcoolicas, command=lambda: self.categorias("alcoolicas"), bg="#FF9933")
        botao_alcoolicas.grid(row=1, column=0, pady=20, padx=50, sticky="ne")
        desc_alcoolicas = tk.Label(self.menu_window, text="BEBIDAS ALCOÓLICAS", font=("Arial", 10), bg="#FF9933")
        desc_alcoolicas.grid(row=2, column=0, sticky="ne", padx=30)

        botao_sobremesas = tk.Button(self.menu_window, image=tk_sobremesas, command=lambda: self.categorias("sobremesas"), bg="#FF9933")
        botao_sobremesas.grid(row=3, column=0, pady=20, padx=50, sticky="ne")
        desc_sobremesas = tk.Label(self.menu_window, text="SOBREMESAS", font=("Arial", 10), bg="#FF9933")
        desc_sobremesas.grid(row=4, column=0, sticky="ne", padx=60)

        botao_menu_chef = tk.Button(self.menu_window, image=tk_menu_chef, command=lambda: self.categorias("menu-chef"),bg="#FF9933")
        botao_menu_chef.grid(row=5, column=0, pady=20, padx=50, sticky="ne")
        desc_menu_chef = tk.Label(self.menu_window, text="MENU DO CHEF", font=("Arial", 10), bg="#FF9933")
        desc_menu_chef.grid(row=6, column=0, sticky="ne", padx=50)

        botao_pedidos = tk.Button(self.menu_window, image=tk_pedidos, command=self.finalizar_pedido,bg="#FF9933")
        botao_pedidos.grid(row=7, column=0, pady=20, padx=50, sticky="s")
        desc_pedidos = tk.Label(self.menu_window, text="CONFIRMAR PEDIDO", font=("Arial", 10), bg="#FF9933")
        desc_pedidos.grid(row=8, column=0, sticky="s", padx=50)

        self.menu_window.mainloop()

    def categorias(self, categoria):
        self.janela_categoria = tk.Tk()
        self.janela_categoria.title(f"{categoria.capitalize()} - Seleção")
        self.janela_categoria.geometry("600x600")
        self.janela_categoria.config(bg="#CC0000")

        tk.Label(self.janela_categoria, text=f"Selecione {categoria.capitalize()}", font=("Arial", 20), bg="#FF9933").pack(pady=20)

        produtos = {
            "entradas": ["Salada", "Bruschetta", "Crostini", "Sopa", "Queijo Assado"],
            "pratos": ["Espaguete", "Bife", "Frango", "Peixe", "Pizza"],
            "bebidas": ["Coca-Cola", "Suco de Laranja", "Água", "Refrigerante", "Chá"],
            "alcoolicas": ["Cerveja", "Vinho", "Whisky", "Caipirinha", "Margarita"],
            "sobremesas": ["Tiramisu", "Cheesecake", "Brownie", "Sorvete", "Frutas"],
            "menu-chef": ["Risoto", "Paella", "Sushi", "Lasanha", "Fondue"]
        }

        for produto in produtos[categoria]:
            tk.Button(self.janela_categoria, text=produto, font=("Arial", 14), command=lambda p=produto: self.adicionar(p), bg="#FF9933").pack(pady=10)

        tk.Button(self.janela_categoria, text="Finalizar Pedido", font=("Arial", 14), command=self.finalizar_pedido, bg="#FF9933").pack(pady=20)

    def adicionar(self, produto):
        self.pedidos.append(produto)
        messagebox.showinfo("Adicionado", f"{produto} foi adicionado ao seu pedido.")

    def finalizar_pedido(self):
        self.janela_categoria.destroy()
        self.janela_pedido = tk.Tk()
        self.janela_pedido.title("Seu Pedido")
        self.janela_pedido.geometry("600x600")
        self.janela_pedido.config(bg="#CC0000")

        tk.Label(self.janela_pedido, text="Seu Pedido", font=("Arial", 20), bg="#FF9933").pack(pady=20)

        self.lista_pedidos = tk.Listbox(self.janela_pedido, selectmode=tk.SINGLE, bg="#FF9933")
        self.lista_pedidos.pack(pady=20)

        for item in self.pedidos:
            self.lista_pedidos.insert(tk.END, item)

        tk.Button(self.janela_pedido, text="Remover Item Selecionado", command=self.remover_item, bg="#FF9933").pack(pady=10)
        tk.Button(self.janela_pedido, text="Adicionar Mais Itens",  bg="#FF9933", command=lambda: [self.janela_pedido.destroy(), self.menu()]).pack(pady=10) #erro não solucionado, fica para a versão 1.1 de forma resumida a função menu exige usuario na entrada e nessa chamada não passa usuario de forma nativa.
        tk.Button(self.janela_pedido, text="Confirmar Pedido", command=self.confirmar_pedido, bg="#FF9933").pack(pady=10)

    def remover_item(self):
        selecionado = self.lista_pedidos.curselection()
        if selecionado:
            index = selecionado[0]
            item = self.lista_pedidos.get(index)
            self.pedidos.remove(item)
            self.lista_pedidos.delete(index)
            messagebox.showinfo("Removido", f"{item} foi removido do seu pedido.")
        else:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para remover.")

    def confirmar_pedido(self):
        self.janela_pedido.destroy()
        self.janela_confirmacao = tk.Tk()
        self.janela_confirmacao.title("Pedido Confirmado")
        self.janela_confirmacao.geometry("400x100")
        self.janela_confirmacao.config(bg="#CC0000")
        tk.Label(self.janela_confirmacao, text="OBRIGADO PELO PEDIDO", font=("Arial", 20), bg="#FF9933").pack(pady=20)
        
        self.janela_confirmacao.mainloop()
        def mostrar_obrigado():
            janela_imagem = tk.Tk()
            janela_imagem.title("Obrigado")
            janela_imagem.geometry("600x600")
            janela_imagem.config(bg="#CC0000")
            imagem = Image.open("C:/Users/PauloSouza/Desktop/Restaurante/obrigado.png")
            imagem_tk = ImageTk.PhotoImage(imagem)    
            label_imagem = tk.Label(janela_imagem, image=imagem_tk)
            label_imagem.image = imagem_tk  
            label_imagem.pack()  
            janela_imagem.mainloop()
        mostrar_obrigado()
Sistema()




    


