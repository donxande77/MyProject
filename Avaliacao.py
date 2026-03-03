# Avaliando Filmes 
print("Digite o nome de um Filme ou Série:")
FS = input()
print("Qual sua nota para avaliar?")
NOTA = int(input())

match NOTA:
    case 1:
        print("Péssimo")
    case 2:
        print("Ruim!")
    case 3:
        print("Razoavel!")
    case 4:
        print("Bom!")
    case 5:
        print("Ótimo!")
    case _:
        print("Alerta!")