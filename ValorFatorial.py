# Demonstração de Valor Fatorial...
n = int(input("Digite um número: "))

if n < 0 or n > 25:
    print("Valor inválido! O número deve estar entre 0 e 25.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print("O fatorial de", n, "é", fatorial)