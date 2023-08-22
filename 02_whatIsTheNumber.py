import random

secret_number = random.randint(1, 10)

tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
    tentativas += 1

    if palpite < secret_number:
        print("Tente um número mais alto.")
    elif palpite > secret_number:
        print("Tente um número mais baixo")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    
