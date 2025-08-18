# print("Olá mundo")

# numero_inteiro = 10
# numero_float = 10.5
# numero_complexo = 1 + 2j

# print(numero_inteiro)
# print(numero_float)
# print(numero_complexo)
# print(type(numero_inteiro))
# print(type(numero_float))
# print(type(numero_complexo))

# divisao = 10 / 3
# print(divisao)
# print(type(divisao))

# int(divisao)
# print(int(divisao))
# print(type(int(divisao)))

##################################
# print("########### Strings ###########")
##################################

# nome = "João"
# sobrenome = 'Silva'
# print(nome)
# print(sobrenome)
# print(type(nome))
# print(type(sobrenome))

# nome_completo = nome + " " + sobrenome
# print("nome_completo", nome_completo)
# print("count", nome_completo.count("a"))
# print(nome_completo.upper())
# print(nome_completo.lower())
# print(nome_completo.replace("João", "Maria"))
# print(nome_completo.find("Silva"))
# print("João" in nome_completo)
# print("Maria" in nome_completo)
# print(len(nome_completo))
# print(nome_completo[0])
# print(nome_completo[1])
# print(nome_completo[0:4])
# print(nome_completo[5:10])
# print(nome_completo.encode())
# print(nome.encode().decode())
# print(nome_completo.split(" "))
# print(nome_completo.join(["Ana", "Oliveira"]))
# print(nome_completo.strip("a"))
# print(nome_completo.startswith("João"))
# print("João" in nome_completo)
# print("Maria" not in nome_completo)


##################################
# print("########### Listas ###########")
##################################

# lista = [1, 2, 3, 4, 5]
# print("lista", lista)
# print("type(lista)  ", type(lista))
# print("lista[0]   ", lista[0])
# print("append lista", lista.append(6))
# print("insert lista", lista.insert(0, 0))
# print("remove lista", lista.remove(3))
# print("pop lista", lista.pop())
# print("sort lista", lista.sort())
# print("reverse lista", lista.reverse())
# print("count lista", lista.count(2))
# print("index lista", lista.index(2))

####################################
# print("########### Tuplas ###########")
# ####################################

# tupla = (1, 2, 2,  3, 4, 5)
# print("tupla", tupla)
# print("type(tupla)  ", type(tupla))
# print("tupla[0]   ", tupla[0])
# print("count tupla", tupla.count(2))
# print("index tupla", tupla.index(2))

##################################
# print("########### Dicionários ###########")
##################################

# dicionario = {
#     "nome": "João",
#     "sobrenome": "Silva",
#     "idade": 30,
#     "altura": 1.75,
#     "enderecos": ["Rua A", "Rua B"],
#     "ativo": True,
# }

# print("dicionario", dicionario)
# print("type(dicionario)  ", type(dicionario))
# print("dicionario['nome']   ", dicionario["nome"])
# print("dicionario['idade']  ", dicionario["idade"])
# print("dicionario['enderecos']  ", dicionario["enderecos"])
# print("dicionario['enderecos'][0]  ", dicionario["enderecos"][0])
# print("dicionario['enderecos'][1]  ", dicionario["enderecos"][1])
# print("keys dicionario", list(dicionario.keys()))
# print("values dicionario", list(dicionario.values()))
# print("items dicionario", list(dicionario.items()))
# print("dicionario.get('nome')", dicionario.get("nome"))
# print("dicionario.get('telefone')", dicionario.get("telefone", "Não encontrado"))
# print("dicionario.pop('idade')", dicionario.pop("idade"))
# print("dicionario após pop", dicionario)
# print("dicionario.update({'idade': 31})", dicionario.update({"idade": 31}))
# print("dicionario após update", dicionario)
# print("dicionario.clear()", dicionario.clear())
# print("dicionario após clear", dicionario)


##########################################
### print("########### For ###########
##########################################

# lista = [1, 2, 3, 4, 5]
# for numero in lista:
#     print("numero", numero)

# for i in range(10):
#     print("i", i)

# dicionario = {
#     "nome": "João", 
#     "sobrenome": "Silva",
#     "idade": 30,
#     }

# for chave in dicionario.keys():
#     print("chave", chave)

# for valor in dicionario.values():
#     print("valor", valor)

# for chave, valor in dicionario.items():
#     print("chave", chave, "valor", valor)


############################################
# print("########### While ###########")
############################################

# contador = 0
# while contador < 10:
#     print("contador", contador)
#     contador += 1


############################################
print("Funções")
############################################

def saudacao(nome):
    """Função que retorna uma saudação personalizada."""
    return f"Olá, {nome}!"
def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b

print(saudacao("João"))
print(soma(5, 3))