print("********************************")
print("Bem vindo no jogo de Adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3


# O "WHILE" TORNA UMA REPETIÇÃO
for rodada in range(1, total_de_tentativas + 1):
  print(f"Tentativa {rodada} de: {total_de_tentativas}")
  chute = int(input("Digite um número: "))
  acertou = chute == numero_secreto
  maior = chute > numero_secreto


  if(acertou):
    print("Você acertou!")
  elif(maior):
    print("Você errou! Seu chute foi acima")
  else:
    print("Você errou! Seu chute foi abaixo")
    
  
  
print("Fim do jogo!")