tupla1 = (1,3,5)
tupla2 = (5,1,3)

# Verificando se as tuplas possuem os mesmos elementos através do set
def verifica_tuplas(tupla1, tupla2):
    if set(tupla1) == set(tupla2):
        print("As tuplas possuem os mesmos elementos")
    else:
        print("As tuplas não possuem os mesmos elementos")

verifica_tuplas(tupla1, tupla2)