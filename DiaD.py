# Programa dirá o que fazer durante a semana...
print("Digite um dia da semana:")
DIA = input()

match DIA:
    case "domingo":
        print("Descanse.")
    case "segunda":
        print("Vá ao médico")
    case "terça":
        print("Vá a academia")
    case "quarta":
        print("Assista TV")
    case "quinta":
        print("Estudar")
    case "sexta":
        print("Ir a praia")
    case "sabado":
        print("Jogue futebol")
    case _:
        print("Alerta!")
        