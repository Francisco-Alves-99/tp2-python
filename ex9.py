def verifica_palindromo():
    texto = input("Digite uma palavra ou uma frase: ")

    textoVeriicado = texto.replace(" ", "").lower() # retira os espaços e transorma em lower case

    # veriica se o texto de trás para frente é o mesmo
    if textoVeriicado == textoVeriicado[::-1]:
        print("é um palíndromo")
    else:
        print("não é um palíndromo")

verifica_palindromo()            