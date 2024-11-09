lista = [1,2,3,4,5,6]

def verifica_par_de_numeros(lista):

    lista.sort() # ordena a lista

    # inicializacao das variaveis: esquerda no começo da lista e direita no final, melhor_soma o maior número possível e pares com valores nulos
    esquerda, direita = 0, len(lista) - 1
    melhor_soma = float('inf')
    pares = (None, None)

    # busca os dois números cuja soma é mais próxima de zero
    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]

        # verifica se encontrou uma soma mais próxima de zero
        if soma < melhor_soma:
            melhor_soma = soma
            pares = (lista[esquerda], lista[direita])

        # ajusta os ponteiros da lista
        if soma < 0:
            esquerda += 1
        else:
            direita -= 1

    print(pares)

verifica_par_de_numeros(lista)    