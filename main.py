def run_task_manager():
    tasks = []
    next_id = 1

    def add_task():
        nonlocal next_id
        description = input("Digite a descrição da nova tarefa: ").strip()
        if description:
            task = {
                "id": next_id,
                "description": description,
                "status": "Pendente"
            }
            tasks.append(task)
            print(f"Tarefa '{description}' adicionada com sucesso! (ID: {next_id})")
            next_id += 1
        else:
            print("A descrição da tarefa não pode ser vazia.")

    def list_tasks():
        if not tasks:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\n--- Lista de Tarefas ---")
        for task in tasks:
            print(f"ID: {task['id']} | Descrição: {task['description']} | Status: {task['status']}")
        print("------------------------")

    def complete_task():
        if not tasks:
            print("Nenhuma tarefa para marcar como concluída.")
            return

        list_tasks() # Mostra as tarefas para o usuário escolher o ID
        try:
            task_id_to_complete = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
        except ValueError:
            print("ID inválido. Por favor, digite um número.")
            return

        found = False
        for task in tasks:
            if task['id'] == task_id_to_complete:
                found = True
                if task['status'] == "Concluída":
                    print(f"A tarefa (ID: {task_id_to_complete}) já está concluída.")
                else:
                    task['status'] = "Concluída"
                    print(f"Tarefa (ID: {task_id_to_complete}) marcada como 'Concluída' com sucesso!")
                break
        
        if not found:
            print(f"Tarefa com ID {task_id_to_complete} não encontrada.")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        print("----------------------")

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print("Saindo do sistema de gerenciamento de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Para executar o sistema, chame a função:
run_task_manager()