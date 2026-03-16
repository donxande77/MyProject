# Caixa eletrônico
valor = int(input("Digite o valor a ser sacado: "))

print("100:", valor // 100)
print("50 :", (valor % 100) // 50)
print("20 :", (valor % 50) // 20)
print("10 :", (valor % 20) // 10)
print("5  :", (valor % 10) // 5)
print("2  :", (valor % 5) // 2)
print("1  :", valor % 2)