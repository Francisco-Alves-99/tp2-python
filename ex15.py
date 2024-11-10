def imprime_mensagem(nome, idade, cidade='Desconhecida'):
    if cidade == 'Desconhecida': # caso em que o parametro de cidade nao é informado
        print(f"{nome} tem {idade} anos e o local de moradia não foi informado.") 
    else: # caso em que o parametro de cidade é informado
        print(f"{nome} tem {idade} anos e mora em {cidade}")    

imprime_mensagem("maria", 30, "sao paulo") # chamada da funcao