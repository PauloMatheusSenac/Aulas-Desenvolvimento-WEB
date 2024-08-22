# Instruções

# Crie uma classe que aceite a digitação de dois números e realize a divisão entre eles, exibindo o resultado.​

# Trate as seguintes exceções:​

# ArithmeticException quando ocorrer uma divisão por zero.​

# ValueError  quando o valor informado não for numérico​


class Divisao:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0

    def exibir_resultado(self):
        if self.obter_numeros():
            resultado = self.realizar_divisao()
            if resultado is not None:
                print(f"O resultado da divisão é: {resultado}")

    def obter_numeros(self):
        try:
            self.numero1 = float(input("Digite o primeiro número: "))
            self.numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, insira um valor numérico.")
            return False
        return True

    def realizar_divisao(self):
        if self.numero2 == 0:
            print("Erro: Não é possível dividir por zero.")
            return None
        return self.numero1 / self.numero2

divisao = Divisao() 
divisao.exibir_resultado()
