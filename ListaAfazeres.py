# Lista de tarefas
tarefas = []

# Cadastro das 5 tarefas
print("=== Cadastro de Tarefas ===")
for i in range(5):
    tarefa = input(f"Digite a descrição da tarefa {i+1}: ")
    tarefas.append(tarefa)

# Exibir lista inicial
print("\nLista de tarefas:")
for i, t in enumerate(tarefas, start=1):
    print(f"{i}. {t}")

# Verificar se a primeira tarefa foi executada
resposta = input("\nA primeira tarefa foi executada? (S/N): ").strip().upper()

if resposta == 'S':
    # Remove a primeira tarefa
    removida = tarefas.pop(0)
    print(f"\nTarefa '{removida}' removida da lista.")

    # Pergunta se deseja adicionar nova tarefa
    nova = input("Deseja adicionar uma nova tarefa? (S/N): ").strip().upper()
    
    if nova == 'S':
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)

# Exibir lista final
print("\n=== Lista Final de Tarefas ===")
for i, t in enumerate(tarefas, start=1):
    print(f"{i}. {t}")