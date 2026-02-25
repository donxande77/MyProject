# Demonstração de variáveis...
MyName = "Alexandre Morais"
MyHeight = 1.90
MyAge = 26
MyAddress = "Santa Cruz"
MyWeight = 98.5
MyTeam = "Flamengo"
MySport = "Futebol"
#Exibição do conteúdo das variáveis...
print("Meu Nome é", MyName)
print("A minha altura é", MyHeight, "metros.")
print("Minha idade é", MyAge, "Anos.")
print("Meu endereço é", MyAddress, "Endereço.")
print("Meu peso é", MyWeight, "Peso.")
print("Meu Time é", MyTeam, "Time.")
print("Meu Esporte é", MySport, "Esporte.")



#Imputação de dados em variáveis... Str de números inteiros e flutuantes precisam ser declarados int(inteiro), float(flutuante)- (input permite inserir dados)-(variável vai armazenar as informações inseridas pelo usuário)
print("Digite o seu nome:")
MyName = input()
print("Digite a sua altura:")
MyHeight = float(input())
print("Digite sua idade:")
MyAge = int(input())
print("Digite seu endereço:")
MyAddress = input()
print("Digite seu peso:")
MyWeight = float(input())
print("Digite seu time:")
MyTeam = input()
print("Digite seu esporte:")
MySport = input()



#Exibição do conteúdo das variáveis...
print("Meu nome é", MyName)
print("A minha altura é", MyHeight)
print("Minha idade é", MyAge)
print("Meu endereço é", MyAddress)
print("Meu peso é", MyWeight)
print("Meu Time é", MyTeam)
print("Meu esporte é", MySport)

print(type(MyName))
print(type(MyHeight))
print(type(MyAge))
print(type(MyAddress))
print(type(MyWeight))
print(type(MyTeam))
print(type(MySport))
