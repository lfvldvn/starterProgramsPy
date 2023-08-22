while True:
    nome = input("Olá, qual o seu nome?")
    if nome:
        break   # Sai do loop se um nome válido for inserido

    print("O nome é obrigatório. Por favor, digite o seu nome.")

print("Olá,", nome, "! Bem-vindo!")

