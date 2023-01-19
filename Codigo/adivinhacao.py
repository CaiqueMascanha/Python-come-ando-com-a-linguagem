import random

print("********************************")
print("Bem vindo no jogo de Adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
print(numero_secreto)

# O "WHILE" TORNA UMA REPETIÇÃO
for rodada in range(1, total_de_tentativas + 1):
  print(f"Tentativa {rodada} de: {total_de_tentativas}")
  chute = int(input("Digite um número entre 1 e 100: "))
  acertou = chute == numero_secreto
  maior = chute > numero_secreto

  if(chute < 1 or chute > 100):
    print("Você deve digitar um número entre 1 e 100!")
    continue #COM ESTE COMENDO NÃO ENCERRA O LAÇO
  
  if(acertou):
    print("Você acertou!")
    break #COM ISSO ENCERRAMOS O LAÇO
  elif(maior):
    print("Você errou! Seu chute foi acima")
  else:
    print("Você errou! Seu chute foi abaixo")
    
  
  
print("Fim do jogo!")
