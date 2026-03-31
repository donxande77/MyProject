# Demostração de métodos em listas...
INSS = ["Maria", "Manoel", "José", "Isabela"]
print("Eis, a fila do INSS:", INSS)

NOVO = input("Insira mais uma pessoa:")
INSS.append(NOVO)
print("conferindo a nova lista: ", INSS)

print("Vou tirar a última pessoa dessa lista...")
ESPECIAL = INSS.pop()

print("Agora, vou colocá-la na frente de todos!")
INSS.insert(0, ESPECIAL)
print("Conferindo a lista:", INSS)

print("Maria não gostou e reclamou...")
INSS.remove("Maria")
print("E agora, ela saiu 'Pê da vida'", INSS)

print("Para não ter mais reclamação, vamos atender...")
INSS.sort()
print("... em ordem alfabética:", INSS)

print("Onde está esta nova pessoa chamada", ESPECIAL, "?")
print("Ela agora ficou na posição", INSS.index(ESPECIAL)+1, "!")
