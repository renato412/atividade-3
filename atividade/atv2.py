nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
while nome == senha:
    print("Nome e senha não podem ser iguais, digite novamente")
    nome = input("Digite novamente seu nome: ")
    senha = input("Digite novamente sua senha: ")
    