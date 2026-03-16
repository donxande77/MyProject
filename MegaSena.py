# Mega Sena
numeros = []

for i in range(6):
    num = int(input("Digite um número: "))

    if num in numeros:
        print("Número repetido")
    else:
        numeros.append(num)

print("Números escolhidos:", numeros)