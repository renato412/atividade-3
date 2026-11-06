maior = int(input("Insira o 1º número: "))

for i in range(2, 6):
    num = int(input(f"Insira o {i}º número: "))

soma = num + maior
media = soma / 5
print("o soma dos numeros é:", soma)
print("a media dos numeros é:", media)
