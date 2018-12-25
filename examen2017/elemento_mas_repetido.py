# -*- coding: utf-8 -*-

def maxNros(nro1, nro2):
    if nro1 > nro2 :
        max = nro1
    else:
        max = nro2
    return max

def elemMasRep(listaOrdenada):
    long = len(listaOrdenada)
    i=0
    max=0
    elemMax=listaOrdenada[0]
    while i<long:
        j=i+1
        maxAux=0
        if j<long:
            while listaOrdenada[i]==listaOrdenada[j]:
                maxAux=maxAux+1
                j=j+1
            if i==0:
                max = maxAux
            elif maxAux > max:
                max = maxAux
                elemMax=listaOrdenada[i]
        i=j

    return elemMax

lista = [1,2,3,3,3,4,4,5]
rv = elemMasRep(lista)
print rv
