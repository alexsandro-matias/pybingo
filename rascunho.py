import random


def criacao_cartela():
    rascunho_cartela = set()
    b = []
    i = []
    n = []
    g = []
    o = []
    cartela = {}

    while len(rascunho_cartela) < 24:
        todos_numeros_bingo = random.randint(1, 76)
        rascunho_cartela.add(todos_numeros_bingo)

    while len(b) < 4 and len(i) < 4 and len(n) < 3 and len(g) < 4 and len(o) < 4:
        for numero_do_bingo in rascunho_cartela:
            if 1 <= numero_do_bingo <= 15:
                b.append(numero_do_bingo)
            if 16 <= numero_do_bingo <= 30:
                i.append(numero_do_bingo)
            if 31 <= numero_do_bingo <= 45:
                n.append(numero_do_bingo)
            if 46 <= numero_do_bingo <= 60:
                g.append(numero_do_bingo)
            if 61 <= numero_do_bingo <= 75:
                o.append(numero_do_bingo)

    print(b)
    print(i)
    print(n)
    print(g)
    print(o)

    # print(rascunho_cartela)
    # print(cartela)
    # return sorted(rascunho_cartela)


    return sorted(rascunho_cartela)


a = criacao_cartela()
# print(a)
