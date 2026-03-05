# Programa que diz a classificação de um time
TIME = input("Digite o Nome do time:")
POSICAO = int(input("Digite a posição:"))

if POSICAO == 1:
    print("Campeão!")
elif POSICAO == 2 or POSICAO <= 6:
    print("Libertadores!")
elif POSICAO == 7 or POSICAO <= 12:
    print("Sul-Americana!")
elif POSICAO == 13 or POSICAO <= 16:
    print("Rebaixado!")
else:
    print("Valor inexistente!")
    
