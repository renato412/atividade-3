num1 = int(input("digite o número base: "))
num2 = int(input("digite o número expoente: "))

resultado = 1

for i in range(num2):
     resultado = resultado * num1
     print(f"o resultado é final é: {resultado}")