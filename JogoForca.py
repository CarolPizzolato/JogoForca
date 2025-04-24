#criar um vetor com as palavras
import random
grafico = ['''
           
           -----------
           |         |   
           |           
           |          
           |         
           |         
           --
           '''
           ,
           '''
           -----------
           |         |   
           |         O  
           |         | 
           |         
           |         
           --
           '''
           ,
           '''
           -----------
           |         |   
           |         O  
           |        \|  
           |         |
           |           
           --
           '''
           ,
           '''
           -----------
           |         |   
           |         O  
           |        \|/   
           |         |
           |          
           --
           '''
           ,
           '''
           -----------
           |         |   
           |         O  
           |        \|/   
           |         |
           |        / 
           --
           '''
           ,
            r'''
           -----------
           |         |   
           |         O  
           |        \|/   
           |         |
           |        / \
           --
           '''
           ]


print ("================================")
print ("Bem vindo ao jogo!")
print ("================================")
print ("Tema: Animais")
print (grafico[0])
#lista inicial

#tentar fazer no futuro um selecionador de tema, por enquanto deixar assim
listaTema = ['cachorro', 'gato', 'galinha', 'papagaio', 'macaco', 'jaguar', 'tartaruga']
#lista aleatorizadora
palavra_escolhida = random.choice(listaTema)
#combo de letras escolhidas


letras_erradas = []
letras_certas = []
#determina os _ da frase
letra_tamanho = ['_' for x in palavra_escolhida]
print (*letra_tamanho)
vida = 6

#loop para o jogo
while vida > 0:
    palavra = list(palavra_escolhida)
    
    while True:
        letra_escolhida =  input ("Digite uma letra: ").lower()
        if len(letra_escolhida) == 1 and letra_escolhida.isalpha():
            break
        else:
            print ("\033[0;31mpor favor digite apenas UMA letra\033[0m")
         
    
    #para nao repetir
    if letra_escolhida in letras_certas or letra_escolhida in letras_erradas:
        print ("Letra já escolhida!")
        continue
    
    #para o acerto da palavra
    if letra_escolhida in palavra_escolhida:
        letras_certas.append(letra_escolhida)
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra_escolhida:
                letra_tamanho[i] = letra_escolhida
                print ("\033[92mLetra certa! \033[0m")
            
    else:
        letras_erradas.append(letra_escolhida.lower())
        vida -= 1
        print (grafico[5-vida])
        print ("\033[0;31mLetra errada! Vidas restantes: {} \033[0m".format(vida))
        print (*letra_tamanho)

    #se perder   
    if vida == 0:
        print ("\033[0;31mVoce perdeu! a palavra era {}\033[m".format(palavra_escolhida))
        print (grafico[5])
        break
    
    if "_" not in letra_tamanho:
        print ("\033[92m Parabens! Voce ganhou! \033[0m", palavra_escolhida)
        print (*letra_tamanho)
        break
    #parte de itens ja colocados e afins
    selecionado = letras_certas+letras_erradas
    print ("Palavras já selecionadas:", selecionado)
    print (*letra_tamanho)
    Letras_Selecionadas = letras_certas + letras_erradas
    print (Letras_Selecionadas)
    


            
