# Demonstração do uso de funções...
def APRESENTAR():
    print(f"Meu nome é {MyName}.")
    print(f"Minha altura é {MyHeigh} metros.")
    print(f"Minha idade é {MyAge} anos.")
    return
def CONFERIR(X):
    if X >= 18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
    return

MyName = str(input("Digite o seu nome: "))
MyHeigh = float(input("Digite sua altura: "))
MyAge = int(input("Digite sua idade: "))

APRESENTAR()
CONFERIR(MyAge)
APRESENTAR() 