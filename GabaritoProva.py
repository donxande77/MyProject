# Demonstração da função lista em gabarito de provas...
GABARITO = ['B', 'C', 'A', 'E', 'D']

acertos = 0
respostas_usuario = []

# Entrada de dados
for i in range(5):
    resposta = input(f"Digite a resposta da questão {i+1}: ").upper()
    respostas_usuario.append(resposta)

# Verificação dos acertos
for i in range(5):
    if respostas_usuario[i] == GABARITO[i]:
        acertos += 1

# Resultado final
print(f"Você acertou {acertos} questões.")