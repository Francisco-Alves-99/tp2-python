alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Fernanda", "nota": 9.3},
    {"nome": "João", "nota": 6.8}
]

def ordena_decrescente(alunos):
    n = len(alunos) # tamanho da lista

    for i in range(n): # controla quantas vezes a lista será percorrida
        for j in range(0, n - i - 1): # percorre os elementos adjacentes
            if alunos[j]['nota'] < alunos[j + 1]['nota']:
                # troca os alunos se a nota de j for menor que a de j + 1
                alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]

    # exibe a lista ordenada
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")     

ordena_decrescente(alunos)               