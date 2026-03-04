print("=== Conversor de Temperatura ===")
print("Escolha a conversão desejada:")
print("1 - Celsius para Kelvin")
print("2 - Celsius para Fahrenheit")
print("3 - Kelvin para Celsius")
print("4 - Kelvin para Fahrenheit")
print("5 - Fahrenheit para Celsius")
print("6 - Fahrenheit para Kelvin")

opcao = int(input("Digite o número da opção: "))

if opcao == 1:
    C = float(input("Digite a temperatura em Celsius: "))
    K = C + 273
    print("Resultado:", K, "K")

elif opcao == 2:
    C = float(input("Digite a temperatura em Celsius: "))
    F = C * 1.8 + 32
    print("Resultado:", F, "F")

elif opcao == 3:
    K = float(input("Digite a temperatura em Kelvin: "))
    C = K - 273
    print("Resultado:", C, "C")

elif opcao == 4:
    K = float(input("Digite a temperatura em Kelvin: "))
    F = (K - 273) * 1.8 + 32
    print("Resultado:", F, "F")

elif opcao == 5:
    F = float(input("Digite a temperatura em Fahrenheit: "))
    C = (F - 32) / 1.8
    print("Resultado:", C, "C")

elif opcao == 6:
    F = float(input("Digite a temperatura em Fahrenheit: "))
    K = (F - 32) * 5/9 + 273
    print("Resultado:", K, "K")

else:
    print("Opção inválida!")