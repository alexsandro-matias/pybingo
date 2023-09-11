import random

def criacao_cartela():
    cartela = {}
    b = set()
    i = set()
    n = set()
    g = set()
    o = set()
    while len(b) < 5:
        numero_aleatorio = random.randint(1, 15)
        b.add(numero_aleatorio)
    while len(i) < 5:
        numero_aleatorio = random.randint(16, 30)
        i.add(numero_aleatorio)
    while len(n) < 4:
        numero_aleatorio = random.randint(31, 45)
        n.add(numero_aleatorio)
    while len(g) < 5:
        numero_aleatorio = random.randint(46, 60)
        g.add(numero_aleatorio)
    while len(o) < 5:
        numero_aleatorio = random.randint(61, 75)
        o.add(numero_aleatorio)
    cartela['b'] = b
    cartela['i'] = i
    cartela['n'] = n
    cartela['g'] = g
    cartela['o'] = o

    return cartela


a = criacao_cartela()

print(a)
