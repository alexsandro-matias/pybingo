import random


def criacao_cartela():
    cartela = {}
    b = set()
    i = set()
    n = set()
    g = set()
    o = set()

    def preenchimento_letras(letra, quantidade_numeros, limite_inferior, limite_superior):
        while len(letra) < quantidade_numeros:
            numero_aleatorio = random.randint(limite_inferior, limite_superior)
            letra.add(numero_aleatorio)

    preenchimento_letras(b, 5, 1, 15)
    preenchimento_letras(i, 5, 16, 30)
    preenchimento_letras(n, 4, 31, 45)
    preenchimento_letras(g, 5, 46, 60)
    preenchimento_letras(o, 5, 61, 75)

    cartela['b'] = b
    cartela['i'] = i
    cartela['n'] = n
    cartela['g'] = g
    cartela['o'] = o

    return cartela


a = criacao_cartela()

print(a)


a = criacao_cartela()

print(a)
