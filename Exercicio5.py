
#Acesse uma posição inválida em uma lista e trate a exceção IndexError. ​

listateste = [1,2,3]


teste = int (input("Digite um numero: "))
try:
    valor = listateste[teste]
    print(f"O valor digitado {teste}, esta na lista!!!!")
except IndexError:
    print("Valor testado não esta na lista")
print("Saindo....")

        