# Demonstração com import listas...

# Vai aparecer na tela a lista de programas infantis...
def PROGRAMAS_INFANTIS(): 
    LISTA = [
        "Patrulha Canina",
        "Peppa Pig",
        "Dora Aventureira",
        "Masha e o Urso",
        "Galinha Pintadinha",
        "PJ Masks",
        "Bob Esponja",
        "Show da Luna"
    ]
    print(f"Programas infantis recomendados:")
    for p in LISTA:
        print("-", p)

# Vai aparecer na tela a lista de carros e valores...
def CARROS_VALORES(): 
    CARRO = [
        "Chevrolet Onix - R$:90.000,00",
        "Honda Civic - R$:100.000,00",
        "Hyundai Creta - R$:120.000,00",
        "Volkswagen Traker - R$:80.000,00"
    ]
    print(f"Separei para você uma lista de carros e valores: ")
    for c in CARRO:
        print("-", c)

X = int(input("Digite sua idade:"))

if X < 18:
    print("Você é menor de idade!"), PROGRAMAS_INFANTIS()
else:
    print("Você é maior de idade!"), CARROS_VALORES()


