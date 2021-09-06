# Dividir para Conquistar
# Recursão

# Padrão
def somaPadrao(lista):
	total = 0
	for x in lista:
		total += x
	return total

# Recursiva
# exercicio 4.1 pag 77
def somaRecursiva(lista):
	if len(lista) == 1:
		return lista.pop()
	
	soma = lista.pop()
	return soma + somaRecursiva(lista)

print(somaRecursiva([1,2,3,4]))