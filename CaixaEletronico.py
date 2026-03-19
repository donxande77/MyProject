# Caixa eletrônico
valor = int(input("Digite o valor a ser sacado: "))

print("100:", valor // 100)
print("50 :", (valor % 100) // 50)
print("20 :", (valor % 50) // 20)
print("10 :", (valor % 20) // 10)
print("5  :", (valor % 10) // 5)
print("2  :", (valor % 5) // 2)
print("1  :", valor % 2)




#---------------------------------------------

Saque = int(input("Digite o valor: "))
CONT50, CONT20, CONT10 = 0
while True:
    if SAQUE >= 50:
        CONT50 += 1
        SAQUE = SAQUE - 50
    elif SAQUE >= 20:
        CONT20 += 1
        SAQUE = SAQUE - 20
    elif SAQUE >= 10:
        CONT10 += 1
        SAQUE = SAQUE - 10
    else:
        print("Valor a baixo do mínimo possivel para sacar!")

print(f"Irei receber {CONT50} notas de 50, {CONT20} notas de 20 e {CONT10} notas de 10.")    