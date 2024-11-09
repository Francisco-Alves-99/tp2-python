lista = [1,2,3,4]

def acessa_elemento():
    # continuará executando o código até que a tentativa tenha êxito
    while True:
        try:
            indice = int(input("Digite o índice do elemento que gostaria de acessar: "))

            print(lista[indice])
            break
        except ValueError: # erro de tipo de elemento inserido incorreto
            print("Digite um número inteiro para acessar o elemento desejado")
        except IndexError: # erro de index inválida para acesso de lista
            print("Digite um número de índice válido")

acessa_elemento()                