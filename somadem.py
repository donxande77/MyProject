# Demonstraçõa de condicionais e operadores...
AVALIACAO = (input("Digite a avaliação (A/B/C/D/E):"))

if AVALIACAO:
    if AVALIACAO == "A" or AVALIACAO == "B" or AVALIACAO == "C":
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Você não digitou...")