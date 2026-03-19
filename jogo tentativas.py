import random

numero_secreto = random.randint(0, 10)
tentativas = 4

print("Jogo de Adivinha, diga qual número eu penso!")

while True:
    chute = int(input("Seu número: "))
    
    tentativas = tentativas + 1

    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou! Agora és Sigma")
        print("Tentativas:", tentativas)
        break   
    elif chute > numero_secreto:
        print("Errou beta. ⬇️ Muito alto!")
    else:
        print("Foi longe seu beta. ⬆️ Muito baixo!")
        
