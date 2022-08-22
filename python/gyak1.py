lista = [2, 4, 21, 43, 78, 15, 0, 1, 2, 54, 6, 9,]

def paros(lista):
    x = []
    for sor in lista:
        if sor % 2 == 0:
            x.append(sor)
    return x

paros = paros(lista)
print(paros)

def osszes(lista):
    for sor in lista:
      x = len(lista)
    return x

osszes = osszes(lista)
print(osszes)

def legnagyobb(lista):
    for sor in lista:
        x = max(lista)
    return x

legnagyobb = legnagyobb(lista)
print(legnagyobb)

def legkisebb(lista):
    for sor in lista:
        x = min(lista)
    return x

legkisebb = legkisebb(lista)
print(legkisebb)

