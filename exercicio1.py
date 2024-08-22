while True:
    try:
        x = int(input("Digite um numero: "))
    except Exception as a:
        print("Eu falei numero po, custa digitar certo?")
        print(f"O tipo de erro foi {a.__class__}")
    except :
        print("Eu falei numero po, custa digitar certo?")
        print(f"O tipo de erro foi {a.__class__}")
    else: 
        print("deu certoooooo")
    finally:
        print("Obrigado, de nada!!!!!!!!")  



