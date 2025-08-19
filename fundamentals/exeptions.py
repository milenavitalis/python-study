print("Exemplo de captura excções")
try:
  numberInt = int(input("Digite um número inteiro:"))
  result = 10 / numberInt
except ValueError as e:
  print(f"Erro de value error: {e}")
  raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
  print(f"Erro: {e}")
else:
  print(f"Resultado: {result}")
finally:
  print("Operação finalizada")