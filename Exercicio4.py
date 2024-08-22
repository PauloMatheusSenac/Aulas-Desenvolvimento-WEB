# Acesse um dicionário com uma chave inexistente e trate a exceção KeyError. ​

animais = {"Dog": "Cachorro", "Cat": "Gato", "Bird": "Passaro"}
teste = input("Digite o nome de um animal (ex: Dog, Cat, Bird): ")
try:
    valor = animais[teste]
    print(f"A tradução de {teste} é {valor}.")
except KeyError:
    print("CADI????????? Não tem não, fih!!!!!")
print("Saindo .....")


