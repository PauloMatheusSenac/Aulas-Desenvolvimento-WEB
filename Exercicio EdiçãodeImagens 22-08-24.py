import tkinter as tk
from tkinter import messagebox


tela = tk.Tk()
imagem1 = tk.PhotoImage(file="C:/Users/PauloSouza/Downloads/cachorro.png" )
imagem2 = tk.PhotoImage(file="C:/Users/PauloSouza/Downloads/gato.png")
imagem3 = tk.PhotoImage(file="C:/Users/PauloSouza/Downloads/tartaruga.png")
imagem4 = tk.PhotoImage(file="C:/Users/PauloSouza/Downloads/papagaio.png")

cachorro = tk.Label(tela, image=imagem1, width=200, height=200)
cachorro.grid(row=0, column=0)
texto_cachorro = tk.Label( text="Comentario:")
texto_cachorro.grid(row=0, column=1)
coment_cachorro = tk.Entry(tela)
coment_cachorro.grid(row=0, column=2)
gato = tk.Label(tela, image=imagem2, width=200, height=200)
gato.grid(row=1, column=0)
texto_gato = tk.Label( text="Comentario:")
texto_gato.grid(row=1, column=1)
coment_gato = tk.Entry(tela)
coment_gato.grid(row=1, column=2)
tartaruga = tk.Label(tela, image=imagem3, width=200, height=200)
tartaruga.grid(row=2, column=0)
texto_tartaruga = tk.Label( text="Comentario:")
texto_tartaruga.grid(row=2, column=1)
coment_tartaruga = tk.Entry(tela)
coment_tartaruga.grid(row=2, column=2)
papagaio = tk.Label(tela, image=imagem4, width=200, height=200)
papagaio.grid(row=3, column=0)
texto_papagaio = tk.Label( text="Comentario:")
texto_papagaio.grid(row=3, column=1)
coment_papagaio = tk.Entry(tela)
coment_papagaio.grid(row=3, column=2)


tela.mainloop()



