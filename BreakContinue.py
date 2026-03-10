# Demonstração do uso de estrutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
    print("DIgite um número negativo para sair:")
    NUMERO = int(input())
    continue
    print ("este texto não será exibido! Mas...")
else: 
    print("O número digitado foi:", NUMERO)