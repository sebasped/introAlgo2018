# -*- coding: utf-8 -*-


# implementa merge sort

def mergeAux(listaIzq,listaDer):

    longIzq = len(listaIzq)
    longDer = len(listaDer)
    i = 0
    j = 0
    listaComb = []

    while ( i < longIzq  and  j < longDer ) :
        if listaIzq[i] > listaDer[j] :
            listaComb.append(listaDer[j])
            j = j + 1
        else :
            listaComb.append(listaIzq[i])
            i = i + 1

    if i < longIzq :
        listaComb = listaComb + listaIzq[i:]
    if j < longDer :
        listaComb = listaComb + listaDer[j:]

    return listaComb


def mergeSort(lista):
    # precondición: lista no vacía.
    long = len(lista)

    if long == 1 : #caso base conquer
        RV = lista
    else :
        #divide
        med = long/2
        #conquer
        listaIzq = mergeSort(lista[0:med])
        listaDer = mergeSort(lista[med:])
        #combine
        RV = mergeAux(listaIzq,listaDer)

    return RV


lista2 = [0,1,3,8,10,24]
lista1 = [2,3,5,8]
# lista1 = [2,4,5,11]

lista = mergeAux([1,4], [2,5])
print lista
# lista = mergeSort([1,18,4,22,4,5,0,10])
lista = mergeSort([10,1,1])
print lista
