# Atividade de saldo em conta...
print("Digite o saldo da sua conta:")
TV = int(input())

if TV <= 7500:
    print("Saldo insuficiente!")
    print("Você não poderá efetuar essa compra!")
else:
    print("Saldo Suficiente!")
    print("Você poderá efetuar essa compra!")