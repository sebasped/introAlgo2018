# -*- coding: utf-8 -*-

#intercambia los elementos de las posiciones 1 y 2
def intercambiar(lista,pos1,pos2):
    ele1 = lista[pos1]
    ele2 = lista[pos2]
    lista[pos1] = ele2
    lista[pos2] = ele1

    #o alternativamente
    #ele1 = lista[pos1]
    #lista[pos1] = lista[pos2]
    #lista[pos2] = ele1


# para cada i, busco el menor elem de lista[i:] y lo pongo en lista[i]
def selectionSort(lista):
    #listaOrdenada = lista[:] #devuelvo una copia ordenada
    i = 0
    longitud = len(lista)

    while i < longitud:
        posMin = i
        j = i + 1

        while j < longitud:
            # if listaOrdenada[j] < listaOrdenada[posMin]:
            if lista[j] < lista[posMin]:
                posMin = j
            j = j + 1

        # intercambiar(listaOrdenada,i,posMin)
        intercambiar(lista,i,posMin)
        i = i + 1

    #return listaOrdenada


#para cada i, mover lista[i] a su posición correcta (lista[0:i] queda ordenada)
def insertionSort(lista):
    i = 0
    longitud = len(lista)

    while i < longitud:
        j = i + 1

        while j < longitud:
            if lista[j] < lista[i] :
                intercambiar(lista,i,j)
            j = j + 1

        i = i + 1


#comparar lista[i] con lista[i+1] para cada i, e intercambiarlos si están
# desordenados. Repertir len(lista) veces
def bubbleSort(lista):
    i = 0
    longitud = len(lista)

    while i < longitud:
        j = 0

        while j < longitud-1 :
            if lista[j+1] < lista[j] :
                intercambiar(lista,j,j+1)
            j = j + 1

        i = i + 1



l1 = [13, 5, 56, 16, 8]
l2 = [5, 8, 13, 16, 45, 98]

listaOrdenada = l1[:]
selectionSort(listaOrdenada)
print "selection sort", listaOrdenada

listaOrdenada2 = l1[:]
insertionSort(listaOrdenada2)
print "insertion sort", listaOrdenada2

listaOrdenada3 = l1[:]
bubbleSort(listaOrdenada3)
print "bubble sort", listaOrdenada3
