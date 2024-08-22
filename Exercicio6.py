# Crie uma função que recebe argumentos e trate exceções relacionadas a tipos de argumentos incorretos. ​


def funcaoteste(teste):
    try:
        num = int(teste)
        print(f"O numero {num}, é valido, sendo assim vou fechar!!!!")
        print("Saindo....")
    except ValueError:
        print("Voce não digitou um numero, sendo assim voce não fez o basico.")
        print("Saindo....")

digit = input("Digite numero ou letra para testar o erro: ")
funcaoteste(digit)

