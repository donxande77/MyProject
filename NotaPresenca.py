# Nota e Presença 
NOTA = int(input("Digite a nota:"))
PRESENCA = int(input("DIgite a presença:"))

if NOTA >= 6 and PRESENCA >= 75:
    print("Aprovado!")
elif NOTA < 6 and PRESENCA < 75:
    print("Reprovado!")
else:
    print("Recuperação!")
