# @classmethod
# @staticmethod
# cuidar para não criar muitos métodos estáticos, pois isso pode indicar que a classe não está bem estruturada

class MyClass:
    valor = 10

    def __init__(self, nome) -> None:
        self.nome = nome
    
    # requer uma instância da classe para ser chamado
    def intance_method(self):
        return f"Intance with name: {self.nome}"
    
    # requer a classe para ser chamado, não uma instância
    @classmethod
    def class_method(cls):
        return f"Class MyClass with value: {cls.valor}"
    
    # não requer nem a classe nem uma instância para ser chamado
    @staticmethod
    def static_method():
        return "This is a static method, does not require class or instance."

obj = MyClass(nome="Example")
print(obj.intance_method())  # Chamada de método de instância
print(MyClass.valor)  # Acessando atributo de classe

print(obj.class_method())  # Chamada de método de classe
print("class method ->", MyClass.class_method())  # Chamada de método de classe diretamente na classe

print("static method ->", MyClass.static_method())  # Chamada de método estático diretamente na classe


class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))

configuracao1 = "Toyota, Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


class Matematica:

  @staticmethod
  def somar(a, b):
    return a + b
  
print(Matematica.somar(a=10, b=15))
