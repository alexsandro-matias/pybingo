import random


def criacao_cartela():
    rascunho_cartela = set()

    while len(rascunho_cartela) < 24:
        todos_numeros_bingo = random.randint(1, 76)
        rascunho_cartela.add(todos_numeros_bingo)

    b = []
    i = []
    n = []
    g = []
    o = []
    cartela = {}

    for numero_do_bingo in rascunho_cartela:
        if 1 <= numero_do_bingo <= 15 and len(b) < 5:
            b.append(numero_do_bingo)
        if 16 <= numero_do_bingo <= 30  and len(i) < 5:
            i.append(numero_do_bingo)
        if 31 <= numero_do_bingo <= 45 and len(n) < 4:
            n.append(numero_do_bingo)
        if 46 <= numero_do_bingo <= 60 and len(g) < 5:
            g.append(numero_do_bingo)
        if 61 <= numero_do_bingo <= 75 and len(o) < 5:
            o.append(numero_do_bingo)

    print(b)
    print(i)
    print(n)
    print(g)
    print(o)

    # print(rascunho_cartela)
    # print(cartela)
    return sorted(cartela.items())


a = criacao_cartela()
# print(a)
