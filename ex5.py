notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5} # dicionario de alunos e suas notas

resultado = {'Aprovado': [], 'Reprovado': []} # novo dicionario para exibir os aprovados e reprovados

# função para dividir os alunos de acordo com suas notas
def verifica_notas(notas):
    for aluno, nota in notas.items():
        if nota >= 7:
            resultado['Aprovado'].append(aluno)
        else:
            resultado['Reprovado'].append(aluno)

verifica_notas(notas)
print(resultado)                