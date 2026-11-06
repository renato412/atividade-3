pares = 0
impares = 0

for i in range(1, 11):
    num = int(input(f"Insira o {i}º número: "))
    if num %2 == 0 :
        pares = pares + 1
    else:
        impares = impares + 1

print(f"resultado de quantos números pares tem: {pares}")
print(f"o resultado de quantos números impares tem: {impares}")