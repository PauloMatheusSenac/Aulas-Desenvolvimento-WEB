# import tkinter as tk


# teste = tk.Tk()

# teste.title("Testando")



# janela = tk.Label(teste, text="Olá, Mundo!")
# botao = tk.Button()
# janela.pack(padx=50, pady=50)


# teste.mainloop()





# from tkinter import *
# from tkinter import ttk

# def contar():
#     global contador
#     contador += 1
#     contador_label.config(text=f"Você clicou {contador} vezes")

# contador = 0
# root = Tk()
# frm = ttk.Frame(root, padding=40)
# frm.grid()

# ttk.Label(frm, text="Clique no botão", font=("Arial", 50)).grid(column=0, row=0)


# contador_label = ttk.Label(frm, text=f"Você clicou {contador} vezes")
# contador_label.grid(column=0, row=2)


# botao = ttk.Button(frm, text="Clique aqui", command=contar)
# botao.grid(column=0, row=1)

# root.mainloop()


# import tkinter as tk


# def contar_cliques():
#     global contador
#     contador += 1
#     janela.config(text=f'Cliques: {contador}')


# root = tk.Tk()
# root.title("Contador de Cliques")
# contador = 0
# botao = tk.Button(root, text="Clique aqui", command=contar_cliques)
# botao.pack(pady=20)
# janela = tk.Label(text="Clique no botão!!!!!", padx=0, pady=0)
# janela = tk.Label(root, text=f'Cliques: {contador}')
# janela.pack(pady=20)
# root.mainloop()
