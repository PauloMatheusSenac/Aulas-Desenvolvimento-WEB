# Converta uma string para um tipo numérico (por exemplo, int ou float) e trate exceções caso a conversão falhe.

def conversor(convertendo):
    try:
        numero = int(convertendo)
        print(f"O texto foi convertido para o número inteiro: {numero}")
        print (type(numero))
    except ValueError:
        try:
            numero = float(convertendo)
            print(f"A string foi convertida para float: {numero}")
            print (type(numero))
        except ValueError:
            
            print("Deu ruim, falhou a conversão kkkkk")


convertendo = input("Digite o que vamos tentar converter: ")
conversor(convertendo)     
  