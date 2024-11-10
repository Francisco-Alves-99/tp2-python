import random

def escolher_fruta_para_presentear():
    # Solicita a lista de frutas e as quantidades correspondentes
    frutas_input = input("Digite as frutas disponíveis (separadas por vírgula): ").split(",")
    frutas = [fruta.strip() for fruta in frutas_input]  # Remove espaços extras
    
    while True:
        quantidades_input = input(f"Digite as quantidades das frutas (separadas por vírgula): ").split(",")
        try:
            quantidades = [int(q.strip()) for q in quantidades_input]  # Converte as quantidades para inteiros
            if len(quantidades) == len(frutas):
                break  # Se o número de frutas e quantidades coincidem, sai do loop
            elif len(quantidades) > len(frutas):
                quantidades = quantidades[:len(frutas)]  # Limita a quantidade ao número de frutas
                break
            else:
                print(f"O número de quantidades ({len(quantidades)}) é menor do que o número de frutas ({len(frutas)}).")
                print("Por favor, reescreva a lista de quantidades.")
        except ValueError:
            print("Erro: Você deve digitar números inteiros para as quantidades. Tente novamente.")
    
    # Escolher aleatoriamente uma fruta
    fruta_escolhida = random.choice(frutas)
    
    # Exibe a fruta sorteada
    print(f"A fruta sorteada para o presente é: {fruta_escolhida}")

# Chama a função para rodar o programa
escolher_fruta_para_presentear()
