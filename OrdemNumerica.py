# Programa de Ordem crescente ou decrecente
X = int(input("Digite o valor de X:"))
Y = int(input("Digite o valor de Y:"))
Z = int(input("Digite o valor de Z:"))

if X > Y and Y > Z:
    print("Decrescente")
elif X < Y and Y < Z:
    print("Crescente")
elif X > Z and X < Y:
    print("Eles estão misturados!")
else:
    print("Comando não executado!")