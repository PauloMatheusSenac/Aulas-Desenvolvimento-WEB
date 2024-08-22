import tkinter as tk
from tkinter import messagebox

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