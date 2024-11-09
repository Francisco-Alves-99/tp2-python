import random

numero_magico = random.randint(1, 20) # cria número aleatório

def advinha_numero_magico():
    tentativas = 1

    # enquanto o número de tentativas for igual ou menor a 4 o código é executado
    while tentativas <= 4:
        palpite = int(input("Digite o palpite para adivinhar o número secreto: "))

        # veriica se o palpite foi correto, abaixo ou acima do número mágico
        if palpite == numero_magico:
            print("seu palpite foi correto!")
            break
        elif palpite > numero_magico:
            print("palpite foi acima do número mágico")
        elif palpite < numero_magico:
            print("palpite foi abaixo do número mágico")  

        tentativas+= 1    

    print(' -------------------------')
    if tentativas > 4:
        print('número limite de tentativas atingidos')
    else:
        print('parabéns!!! você acertou o número mágico')        

advinha_numero_magico()        