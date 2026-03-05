# Programa que define a posição do jogador...
FUNCAO = input("Digite a sua Posição:")
    
if FUNCAO == 'goleiro' or 'zagueiro' or 'lateral':
    print("Defesa!")
elif FUNCAO == 'ala' or 'volante' or 'meia':
    print("Meio-Campo!")
elif FUNCAO == 'ponta' or 'atacante' or 'centroavante':
    print("Ataque!")
else:
    print("Teimoso!")