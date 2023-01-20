def jogar():
    print("***************************")
    print("Bem vindo no jogo de Forca!")
    print("***************************")
    
    palavra_secreta = "caju"
    numero_caracteres = len(palavra_secreta)
    print(f"O número de letras é: {numero_caracteres}")
    
    enforcou = False
    acertou = False
    
    #ENQUANDO NÃO ENFORCOU E NÃO ACERTOU
    while(not enforcou and not acertou):
      
      chute = input("Qual letra?")
      chute = chute.strip() #DESSA FORMA TIRA OS ESPAÇOS
      
      index = 0
      for letra in palavra_secreta:
        if(chute.lower() == letra.lower()):
          print(f"Correto! A letra '{letra}' está na posição {index}")
        index = index + 1
      
      print("Jogando...")
      
    print("Fim do jogo!")
  
if(__name__ == "__main__"):
  jogar()
