# -*- coding: utf-8 -*-


#ordena lista con números entre 0 y 9, en O(|list|)
def sort09(lista):

    longitud = len(lista)
    j = 0
    listaOrdenada = []

    while j < 10:
        i = 0
        while i < longitud:
            if lista[i] == j :
                listaOrdenada = listaOrdenada + [j]
            i = i + 1

        j = j + 1

    # print listaOrdenada
    return listaOrdenada


lista1 = [5,4,2,2,0,1,0,8,8,9,7]
lista1Ordenada = sort09(lista1)
print lista1Ordenada
print lista1
