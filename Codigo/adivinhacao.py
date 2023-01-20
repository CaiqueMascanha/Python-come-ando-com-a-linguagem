import random

def jogar():
  print("********************************")
  print("Bem vindo no jogo de Adivinhação")
  print("********************************")

  numero_secreto = random.randrange(1,101)
  total_de_tentativas = 0
  pontos = 1000
  print("Qual o níel de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Define o nível: "))
  if(nivel == 1):
    total_de_tentativas = 20
  elif(nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5
    
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
      print(f"Você acertou e fez {pontos} pontos!")
      break #COM ISSO ENCERRAMOS O LAÇO
    elif(maior):
      print("Você errou! Seu chute foi acima")
    else:
      print("Você errou! Seu chute foi abaixo")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
      
    
    
  print("Fim do jogo!")
  
if(__name__ == "__main__"):
  jogar()
