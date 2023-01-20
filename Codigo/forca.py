def jogar():
    print("***************************")
    print("Bem vindo no jogo de Forca!")
    print("***************************")
    
    palavra_secreta = "banana"
    print("A palavra secreta possui :"len(palavra_secreta))
    
    enforcou = False
    acertou = False
    
    #ENQUANDO NÃO ENFORCOU E NÃO ACERTOU
    while(not enforcou and not acertou):
      
      chute = input("Qual letra?")
      
      index = 0
      for letra in palavra_secreta:
        if(chute == letra):
          print(f"encontrei a letra {letra} na posição {index}")
        index = index + 1
      
      print("Jogando...")
      
    print("Fim do jogo!")
  
if(__name__ == "__main__"):
  jogar()
