import random

numero_secreto = random.randint(0, 10)
tentativas = 1

print("Queres te tornar o novo Rei? então diga qual número eu penso!")

while True:
    chute = int(input("Qual é o número?  "))
    
    tentativas = tentativas + 1

    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou! Agora és o REI!")
        print("Tentativas:", tentativas)
        break   
    elif chute > numero_secreto:
        print("Errou fraco, quase lá. ⬇️ Muito alto!")
    else:
        print("Foi longe fraco, quase lá . ⬆️ Muito baixo!")
        
