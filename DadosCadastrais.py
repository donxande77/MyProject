# Demonstração de dados cadastrais de pacientes...
dados = ["Nome", "Data de nascimento", "Sexo", "Diagnóstico", "Estado", "Tratamento", "Data de liberação"]
ficha = []

# Cadastro dos dados
for campo in dados:
    valor = input(campo + ": ")
    ficha.append(valor)

print("Ficha do paciente")

for i in range(len(dados)):
    print(dados[i] + ":", ficha[i])

alterar = input("Deseja alterar os dados? (sim ou nao): ")

if alterar == "sim":
    for i in range(len(dados)):
        ficha[i] = input(dados[i] + ": ")

print("Ficha atualizada")

for i in range(len(dados)):
    print(dados[i] + ":", ficha[i])
