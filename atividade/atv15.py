n = int(input("Quantos números você deseja inserir no conjunto? "))

soma = 0
maior = None
menor = None

for i in range(1, n + 1):

    while True:
        num = float(input(f"Digite o {i}º número (entre 0 e 1000): "))
        
        
        if 0 <= num <= 1000:
            break
        else:
            print("Número inválido! O valor deve estar estritamente entre 0 e 1000.")

    soma = soma + num
    
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
