from collections import deque

grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []




def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + ' é um vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificas.append(pessoa)
    return False

pesquisa('voce')
