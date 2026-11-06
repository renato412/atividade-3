while True:
    nota = int(input("digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("digite outra nota")
    else:
        break