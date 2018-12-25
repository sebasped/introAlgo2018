# -*- coding: utf-8 -*-

def maxAux(nro1, nro2):
    if nro1 > nro2 :
        max = nro1
    else:
        max = nro2
    return max

#máximo de una lista de enteros positivos usando D & C.
def maximo(lista):

    if len(lista) == 1 :
        maximoActual = lista[0]
    # elif len(lista) == 2 :
        # maximoActual = maxAux(lista[0],lista[1])
    else :
        med = len(lista)/2
        max1 = maximo(lista[0:med])
        max2 = maximo(lista[med:])
        maximoActual = maxAux(max1,max2)

    return maximoActual


res = maximo([1,2,1,18,2,10,11])
print res
