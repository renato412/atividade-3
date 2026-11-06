num1 = int(input("Insira o termo que deseja descobrir: "))
ultimo = 1
penultimo = 1

if num1 == 1 or num1 == 2:
    print("O termo é: 1")
else:
    i = 3
    while i <= num1:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    
        i += 1
        print(termo)