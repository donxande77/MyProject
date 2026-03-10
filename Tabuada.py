# Demonstração do uso de estrutura repetitiva...
# Programa que mostra a tabuada de multiplicação...

numero = int(input("Digite um número: "))

for X in range(1, 11):

    resultado = numero * X
    print(f"{numero} x {X} = {resultado}")


