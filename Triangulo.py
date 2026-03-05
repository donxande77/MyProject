# Programa do triangulo.
DIREITO = int(input("Digite o valor de X:"))
ESQUERDO= int(input("Digite o valor de Y:"))
BAIXO = int(input("Digite o valor de Z:"))

if DIREITO == ESQUERDO and ESQUERDO == BAIXO:
    print("Equilátero")
elif DIREITO == ESQUERDO or ESQUERDO == BAIXO or BAIXO == DIREITO:
    print("Isósceles")
elif DIREITO > BAIXO or DIREITO < ESQUERDO:
    print("Escaleno")
else:
    print("Comando não executado!")