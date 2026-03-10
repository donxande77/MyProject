# Vou me aposentar...
IDADE = int(input("Qual é a idade:"))
INSS = int(input("Quantos anos de contribuição:"))
INSALUBRE = int(input("Em condições insalubre S/N)? "))

if INSALUBRE == "S":
    if INSS >= 25:
        print("Aposentadoria especial!!")
    else:
        print("Faltam", 25 - INSS, "anos para se aposentar...")
        print (f"Faltam {25 - INSS} anos para se aposentar...")
        
else:
    if IDADE >= 65 and INSS >= 35:
        print("Aposentadoria normal.")
    else:
        print("Falta atender os requisitos.")