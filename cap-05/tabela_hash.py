caderno = dict()

caderno["maçâ"] = 0.67
caderno["leite"] = 1.47
caderno["abacate"] = 1.49

print(caderno)

voted = {}
def verifica_eleitor(nome):
  if voted.get(nome):
    print('Mande embora!')
  else:
    voted[nome] = True
    print('Deixe votar!')

verifica_eleitor('mike')
verifica_eleitor('tom')
verifica_eleitor('tom')