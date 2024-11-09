idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16} # criação do dicionário com nomes e idades

# abaixo, função que recebe um dicionário e retorna apenas as pessoas maior de idade
def retorna_maior_idade(dicionario):
    maior_de_idade = {nome:idade for nome, idade in dicionario.items() if idade >= 18}
    return maior_de_idade

print(retorna_maior_idade(idades)) # print com a chamada da função e o retorno dela