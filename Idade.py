# Demonstração do uso de if...
print("Digite a sua idade:")
IDADE= int(input())

if IDADE < 18:
    print("Você não é maior de idade!.")
    print("Você é não poderá realizar operações bancária!")
elif IDADE >= 65:
    print("Você já é aposentado")
    print("Podemos oferecer suporte técnico...")
else:
    print("Você é maior de idade!")
    print("Portanto, poderá realizar operações bancárias!")

print("Obrigado por escolher os nossos serviços!")