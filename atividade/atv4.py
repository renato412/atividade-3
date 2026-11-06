maior = int(input("Insira o 1º número: "))

for i in range(2, 6):
    num = int(input(f"Insira o {i}º número: "))
    
    
    if num > maior:
        maior = num

print("O maior número é:", maior)
