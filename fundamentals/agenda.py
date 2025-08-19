def select_option(contacts):
    list_contacts(contacts)
    print(input("Digite o número do contato que deseja selecionar: "))

def add_contact(contacts):
    name = input("Digite o nome do contato: ")
    if any(contact['name'] == name for contact in contacts):
        print(f"Contato {name} já existe!")
        return

    phone = input("Digite o telefone do contato: ")
    if not phone.isdigit() or len(phone) < 10:
        print("Telefone inválido! Deve conter apenas números e ter pelo menos 10 dígitos.")
        return

    email = input("Digite o email do contato: ")
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Email inválido!")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email, "favorite": False})
    print(f"Contato {name} adicionado com sucesso!")


def list_contacts(contacts):
    if not contacts:
        print("Nenhum contato cadastrado.")
        return

    for i, contact in enumerate(contacts, start=1):
        favorite = "★" if contact['favorite'] else "☆"
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} {favorite}")


def update_contact(contacts):
    list_contacts(contacts)
    index = int(input("Digite o número do contato que deseja atualizar: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Contato inválido!")
        return
    
    types = {"nome": "name", "telefone": "phone", "email": "email"}
    
    field = input("Digite o campo que deseja atualizar (" + ", ".join(types.keys()) + "): ")
    field = field.lower()

    if field not in types:
        print("Campo inválido!")
        return

    field_key = types[field]    
    new_value = input(f"Digite o novo valor para {field}: ")

    if field_key == "name" and any(contact['name'] == new_value for contact in contacts if contact != contacts[index]):
        print(f"Contato {new_value} já existe!")
        return
    if field_key == "phone" and (not new_value.isdigit() or len(new_value) < 10):
        print("Telefone inválido! Deve conter apenas números e ter pelo menos 10 dígitos.")
        return
    if field_key == "email" and ("@" not in new_value or "." not in new_value.split("@")[-1]):
        print("Email inválido!")
        return
    
    contacts[index][field_key] = new_value
    print(f"Contato {contacts[index]['name']} atualizado com sucesso!")

def toggle_favorite(contacts):
    list_contacts(contacts)
    index = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Contato inválido!")
        return
    
    contacts[index]['favorite'] = not contacts[index]['favorite']
    status = "favorito" if contacts[index]['favorite'] else "não favorito"
    print(f"Contato {contacts[index]['name']} agora é {status}.")

def list_favorites(contacts):
    favorites = [contact for contact in contacts if contact['favorite']]
    if not favorites:
        print("Nenhum contato favorito.")
        return

    for i, contact in enumerate(favorites, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} ★")
    if not favorites:
        print("Nenhum contato favorito.")

def delete_contact(contacts):
    list_contacts(contacts)
    index = int(input("Digite o número do contato que deseja excluir: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Contato inválido!")
        return
    
    deleted_contact = contacts.pop(index)
    print(f"Contato {deleted_contact['name']} excluído com sucesso!")
    return deleted_contact


        
contacts = []

while True:
  print("\nMenu gerenciador de agenda")
  print("1 - Adicionar contato")
  print("2 - Listar contatos")
  print("3 - Atualizar contato")
  print("4 - Marcar/desmarcar contato como favorito")
  print("5 - Listar contatos favoritos")
  print("6 - Excluir contato")
  print("7 - Sair")


  option = input("\nEscolha uma opção: ")

  if option == "1":
    add_contact(contacts)
  elif option == "2": 
    list_contacts(contacts)
  elif option == "3": 
    update_contact(contacts)
  elif option == "4":
    toggle_favorite(contacts)
  elif option == "5":
    list_favorites(contacts)
  elif option == "6":
    delete_contact(contacts)
  elif option == "7":
    print("Saindo do gerenciador de agenda.")
    break
  else:
    print("Opção inválida! Por favor, escolha uma opção válida.")
  print("\n") 
