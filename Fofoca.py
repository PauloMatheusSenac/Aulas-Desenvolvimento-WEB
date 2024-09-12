# Crie um modelo usando Tkinter, com banco de dados, que terá 3 tipos de acesso: admin, cliente, famoso. O admin é obrigado a logar para poder criar as fofocas, o cliente não é obrigado a logar e pode só seguir a navegação pela página sem realizar o login, o famoso deve fazer o login para reportar alguma fofoca sobre ele, que ele não tenha gostado.
# O login do cliente serve somente para acumular pontos pela sua leitura frequente de fofocas.
# Cada fofoca criada deve conter: 3 imagens e um textos.


import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import io


def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='10.28.2.59',
            user='suporte',
            password='suporte',
            database='sistema_fofocas'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def mostrar_fofocas():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        query = "SELECT id, texto, imagem1, imagem2, imagem3 FROM fofocas"
        cursor.execute(query)
        fofocas = cursor.fetchall()
        
        janela_fofocas = tk.Toplevel(janela)
        janela_fofocas.title("Fofocas")

        for fofoca_id, texto, img1, img2, img3 in fofocas:
            tk.Label(janela_fofocas, text=texto).pack()

            
            if img1:
                img1 = Image.open(io.BytesIO(img1))
                img1 = ImageTk.PhotoImage(img1)
                tk.Label(janela_fofocas, image=img1).pack()
                janela_fofocas.image1 = img1
            if img2:
                img2 = Image.open(io.BytesIO(img2))
                img2 = ImageTk.PhotoImage(img2)
                tk.Label(janela_fofocas, image=img2).pack()
                janela_fofocas.image2 = img2
            if img3:
                img3 = Image.open(io.BytesIO(img3))
                img3 = ImageTk.PhotoImage(img3)
                tk.Label(janela_fofocas, image=img3).pack()
                janela_fofocas.image3 = img3

        cursor.close()
        conexao.close()


def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        query = "SELECT id, senha, tipo_acesso FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id, senha_armazenada, tipo_acesso = resultado
            if senha_armazenada == senha:
                if tipo_acesso == 'admin':
                    mostrar_tela_admin()
                elif tipo_acesso == 'famoso':
                    mostrar_tela_famoso(usuario_id)
                else:
                    messagebox.showinfo("Login", "Cliente logado com sucesso!")
                    mostrar_fofocas()
            else:
                messagebox.showerror("Erro", "Senha incorreta!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado!")

        cursor.close()
        conexao.close()


def mostrar_tela_admin():
    janela_admin = tk.Toplevel(janela)
    janela_admin.title("Admin - Criar Fofoca")

    tk.Label(janela_admin, text="Texto da Fofoca").pack()
    entry_texto = tk.Entry(janela_admin, width=50)
    entry_texto.pack()

    tk.Label(janela_admin, text="Imagem 1").pack()
    button_img1 = tk.Button(janela_admin, text="Escolher Imagem", command=lambda: escolher_imagem(1))
    button_img1.pack()

    tk.Label(janela_admin, text="Imagem 2").pack()
    button_img2 = tk.Button(janela_admin, text="Escolher Imagem", command=lambda: escolher_imagem(2))
    button_img2.pack()

    tk.Label(janela_admin, text="Imagem 3").pack()
    button_img3 = tk.Button(janela_admin, text="Escolher Imagem", command=lambda: escolher_imagem(3))
    button_img3.pack()

    tk.Button(janela_admin, text="Salvar Fofoca", command=lambda: salvar_fofoca(entry_texto.get())).pack()


def escolher_imagem(imagem_numero):
    global imagem_1, imagem_2, imagem_3
    arquivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if arquivo:
        with open(arquivo, 'rb') as file:
            if imagem_numero == 1:
                imagem_1 = file.read()
            elif imagem_numero == 2:
                imagem_2 = file.read()
            elif imagem_numero == 3:
                imagem_3 = file.read()


def salvar_fofoca(texto):
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO fofocas (texto, imagem1, imagem2, imagem3) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (texto, imagem_1, imagem_2, imagem_3))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Fofoca criada com sucesso!")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao criar fofoca: {e}")
        finally:
            cursor.close()
            conexao.close()


def mostrar_tela_famoso(usuario_id):
    janela_famoso = tk.Toplevel(janela)
    janela_famoso.title("Famoso - Reportar Fofoca")

    tk.Label(janela_famoso, text="ID da Fofoca a Reportar").pack()
    entry_id_fofoca = tk.Entry(janela_famoso)
    entry_id_fofoca.pack()

    tk.Label(janela_famoso, text="Motivo do Relato").pack()
    entry_motivo = tk.Entry(janela_famoso)
    entry_motivo.pack()

    tk.Button(janela_famoso, text="Reportar", command=lambda: reportar_fofoca(usuario_id, entry_id_fofoca.get(), entry_motivo.get())).pack()


def reportar_fofoca(usuario_id, fofoca_id, motivo):
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO reportar_fofocas (usuario_id, fofoca_id, motivo) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (usuario_id, fofoca_id, motivo))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Fofoca reportada com sucesso!")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao reportar fofoca: {e}")
        finally:
            cursor.close()
            conexao.close()


def login_cliente():
    mostrar_fofocas()


janela = tk.Tk()
janela.title("Sistema de Fofocas")

tk.Label(janela, text="Usuário").pack()
entry_usuario = tk.Entry(janela)
entry_usuario.pack()

tk.Label(janela, text="Senha").pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

tk.Button(janela, text="Entrar", command=verificar_login).pack()
tk.Button(janela, text="Login Cliente", command=login_cliente).pack()

imagem_1 = imagem_2 = imagem_3 = None

janela.mainloop()



# -- Criação do banco de dados
# CREATE DATABASE IF NOT EXISTS sistema_fofocas;
# USE sistema_fofocas;

# -- Tabela para armazenar informações dos usuários
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     usuario VARCHAR(50) NOT NULL UNIQUE,
#     senha VARCHAR(255) NOT NULL,
#     tipo_acesso ENUM('admin', 'cliente', 'famoso') NOT NULL
# );

# -- Tabela para armazenar as fofocas
# CREATE TABLE IF NOT EXISTS fofocas (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     texto TEXT NOT NULL,
#     imagem1 LONGBLOB,
#     imagem2 LONGBLOB,
#     imagem3 LONGBLOB
# );

# -- Tabela para armazenar os reportes de fofocas
# CREATE TABLE IF NOT EXISTS reportar_fofocas (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     usuario_id INT NOT NULL,
#     fofoca_id INT NOT NULL,
#     motivo TEXT NOT NULL,
#     FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
#     FOREIGN KEY (fofoca_id) REFERENCES fofocas(id)
# );

# -- Tabela para armazenar os pontos dos clientes (opcional)
# CREATE TABLE IF NOT EXISTS clientes_pontos (
#     usuario_id INT PRIMARY KEY,
#     pontos INT DEFAULT 0,
#     FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
# );
