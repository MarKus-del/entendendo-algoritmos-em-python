# pag 77


# 4.2
# def lentgh(lista):
# 	if len(lista) == 1:
# 		return 1
# 	lista.pop()
# 	return 1 + lentgh(lista)

# print(lentgh(['', '', '', 5, 78, 6.5]))

# 4.3
def maxValueInList(lista, maxValue = 0):
	if len(lista) == 1:
		return lista[0] if lista[0] >= maxValue else maxValue

	item = lista.pop()
	sub_max = maxValueInList(lista, item)
	return item if item >= sub_max else sub_max

print(maxValueInList([1,3,95,8]))