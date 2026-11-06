n1 = int(input("digite o seu primeiro número: "))
n2 = int(input("digite o seu segundo número: "))

soma = 0 

for i in range(n1 , n2, +1):
    print(i)
    soma = soma + i

print("a soma é:", soma)