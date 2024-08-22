import tkinter as tk
from tkinter import messagebox

def contar_cliques():
    global contador
    contador += 1
    janela.config(text=f'Cliques: {contador}')
    if contador > 10:
        contador = 0

def contarimp():
    global cont
    cont += 1
    erros = 0
    print(f'O Botão foi clicado {cont} vezes')
    if cont == 10:
        print("Parabéns, você clicou 10 vezes")
        print(20 * "*")
        print(20 * "*")
        print(20 * "*")
        print(20 * "*")
    elif cont > 10:
        messagebox.showwarning(title="Clicou +10", message="Você clicou mais de 10 vezes!")
        aceita = messagebox.askyesno(title="Assumindo a Culpa", message="Vc entende que clicou a mais ne?")
        if aceita :
            messagebox.showwarning(title="Aceitou", message="Vou resetar, na proxima vez le o que ta escrito po!!!!!")
            cont = 0
            #erros +=1
            #print(erros)
        
        else:
            messagebox.showerror(title="Não aceitou", message="Basta Ler parça")
            sair()
    #if erros == 2:
        #messagebox.showerror(title="Não aceitou", message="Basta Ler parça")
        #sair()    
            

def clicou():
    contar_cliques()
    contarimp()

def sair():
    print("OVO SAIRRRRR")
    tela.quit()


    


tela = tk.Tk()
tela.title("Contador de Cliques")

contador = 0
cont = 0

botao = tk.Button(tela, text="Clique até no máximo 10 vezes", command=clicou, width=50, height=10)
botao.pack(pady=20)

janela = tk.Label(tela, text=f'Cliques: {contador}', font=("Arial", 12))
janela.pack(pady=20)

tela.mainloop()









