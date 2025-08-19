## Exemplo de uso: antes de adicionar um usuário, precisará verificar se o usuário já está autenticado
## Com isso, poderia chamar por exemplo `@auth_required` antes de uma função que adiciona um usuário

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def function():
    print("The function is called.")

function()


### Decorador de classes
class DecoradorClass:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> None:
        print("Something is happening before the class is instantiated.")
        self.func()
        print("Something is happening after the class is instantiated.")


@DecoradorClass
def second_function():
    print("The second function is called.")

second_function()