from collections import Counter

lista = [4, 1, 5, 2, 3, 2, 4, 4]

# Contando os elementos repetidos utilizando o Counter
contagem = Counter(lista)

print(dict(contagem)) # Convertendo o resultado do Counter para um dicionário