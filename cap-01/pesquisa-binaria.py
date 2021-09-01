def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1

	while baixo <= alto:
		meio = int((baixo + alto) / 2)
		chute = lista[meio]

		if chute == item:
			return meio

		if chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1
	return None

minha_lista = [ 1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

# pagina 28 resposta:

# 1.1 : log 2 de 128 = 7 tentativas
# 1.2 : log 2 de 256 = 8 tentativas