import random


# Função para criar um cartão de bingo com números distintos
def criar_cartao_bingo():
    cartao = []
    for i in range(5):
        linha = []
        for _ in range(5):
            num = random.randint(i * 15 + 1, (i + 1) * 15)
            while num in linha:
                num = random.randint(i * 15 + 1, (i + 1) * 15)
            linha.append(num)
        cartao.append(linha)
    return cartao


# Função para exibir um cartão de bingo
def exibir_cartao(cartao):
    for linha in cartao:
        print(linha)


# Função para sortear um número de bingo
def sortear_numero():
    return random.randint(1, 75)


# Função para verificar se o jogador ganhou
def verificar_ganhador(cartao, numeros_sorteados):
    for linha in cartao:
        if all(numero in numeros_sorteados for numero in linha):
            return True
    return False


# Função principal do jogo
def jogo_de_bingo():
    print("Bem-vindo ao jogo de Bingo!")

    # Criar cartão de bingo para o jogador
    cartao_jogador = criar_cartao_bingo()
    print("\nSeu cartão de bingo:")
    exibir_cartao(cartao_jogador)

    # Inicializar lista de números sorteados
    numeros_sorteados = []

    while True:
        input("Pressione Enter para sortear um número...")
        numero_sorteado = sortear_numero()
        print(f"O número sorteado é: {numero_sorteado}")

        numeros_sorteados.append(numero_sorteado)

        if verificar_ganhador(cartao_jogador, numeros_sorteados):
            print("Parabéns! Você ganhou o jogo de Bingo!")
            break

    print("O jogo acabou!")


# Iniciar o jogo de bingo
jogo_de_bingo()