def addTask(tasks, nome_tarefa):
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tasks.append(tarefa)
  print(f"Tarrefa {nome_tarefa} foi adicionada com sucesso!")
  return

def viewTasks(tasks):
  print("\nLista de tarefas:")
  for index, task in enumerate(tasks, start=1):
    status = "✓" if task["completada"] else " "
    nome_tarefa = task["tarefa"]
    print(f"{index}. [{status}] {nome_tarefa}")
  return

def updateTaskName(tasks, indexTask, newNameTask):
  newIndexTask = int(indexTask) - 1
  if newIndexTask >= 0 and newIndexTask < len(tasks):
    tasks[newIndexTask]["tarefa"] = newNameTask
    print(f"Tarefa {indexTask} atualizada para {newNameTask}")
  else:
    print("Índice de tarefas inválido.")
  return

def completeTask(tasks, indexTask):
  newIndexTask = int(indexTask) - 1
  tasks[newIndexTask]["completada"] = True
  print(f"Tarefa {indexTask} marcada como completada")
  return

def deleteTaskComplete(tasks):
  for task in tasks:
    if task["completada"]:
      tasks.remove(task)
  print("Tarefas completadas foram deletadas.")
  return

tasks = []
while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar Tarefas")
  print("4. Completar Tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    addTask(tasks, nome_tarefa)

  elif escolha == "2":
    viewTasks(tasks)

  elif escolha == "3":
    viewTasks(tasks)
    indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    updateTaskName(tasks, indice_tarefa, novo_nome)

  elif escolha =="4":
    viewTasks(tasks)
    indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
    completeTask(tasks, indice_tarefa)

  elif escolha == "5":
    deleteTaskComplete(tasks)
    viewTasks(tasks)

  elif escolha == "6":
    break

print("Programa finalizado")