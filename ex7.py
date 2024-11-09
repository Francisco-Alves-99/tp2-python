turma = {}

def adiciona_alunos():
    fim = False
    # enquanto a variavel 'fim' for false, o código será executado
    while not fim:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        turma[nome] = nota # adiciona no dicionario turma o nome e nota do aluno

        continuar = input("Deseja inserir um novo aluno? (digite 'fim' para finalizar) ")

        # se o usuário digitar 'fim' o código é encerrado
        if continuar.lower() == 'fim':
            fim = True
            print(turma)

adiciona_alunos()            