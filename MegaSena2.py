# Demonstração de chances da mega sena...
import math

# função que calcula a chance (1 em X)
def chance(n):
    return math.comb(60, n)

# testando de 6 a 10 números
for n in range(6, 21):
    c = chance(n)
    prob = 1 / c
    print(f"Aposta com {n} números: 1 em {c:,} | {prob*100:.8f}%")

