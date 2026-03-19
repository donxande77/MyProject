# Demonstração do Jogo par ou impar...
import random

#Número do aleatório do computador...
NUMERO = random.randint(1, 100)  

USUARIO = int(input("Digite um número:"))

TOTAL = NUMERO + USUARIO
print(f"Você escolheu {USUARIO}, o computador escolheu {NUMERO}. Soma = {TOTAL}")

if TOTAL % 2 == 0:
    print("Par! Parabéns, você é o vencedor...")
else:
    print("Impar! Você Perdeu...")

