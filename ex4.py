dicionario1 = {'a': 1, 'b': 2}
dicionario2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Verificando se o primeiro dicionario é um subconjunto do segundo
def verifica_dicionarios(dicionario1, dicionario2):
    if dicionario1.items() <= dicionario2.items():
        print("o primeiro dicionario é um subconjunto do segundo")
    else:
        print("o primeiro dicionario não é um subconjunto do segundo")    

verifica_dicionarios(dicionario1, dicionario2)