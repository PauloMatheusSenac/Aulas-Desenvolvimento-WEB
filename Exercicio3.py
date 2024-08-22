# Crie uma exceção personalizada (subclasse de Exception) com uma mensagem específica. Use essa exceção em um contexto relevante.​

class ValorInvalido(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

def solicitar_numero():
    while True:
        try:
            teste = int(input("Digite um número entre 1 e 100: "))
            if teste < 1 or teste > 100:
                raise ValorInvalido(f"Eu falei entre 1 e 100 e vc digitou {teste}, ta de brincadeira ne???? Digita certo ae!.")
            break
        except ValueError:
            print("Tu errou pó, so pode numero inteiro!")
        except ValorInvalido as e:
            print(e)
    
    print("Parabens, acertou. Obrigado!")

solicitar_numero()



