# -*- coding: utf-8 -*-


#cuenta cantidad de elementos repetidos en ambas listas. Las listas están
#ordenadas
def enAmbasListas(lista1, lista2):

    long1 = len(lista1)
    long2 = len(lista2)
    i = 0
    j = 0
    cantRep = 0

    while ( i < long1  and  j < long2 ) :
        if lista1[i] > lista2[j] :
            j = j + 1
        else :
            if lista1[i] == lista2[j] :
                cantRep = cantRep + 1
            i = i + 1

    return cantRep


lista2 = [0,1,3,8,10,24]
lista1 = [2,3,5,8]
# lista1 = [2,4,5,11]

cantRep = enAmbasListas(lista1, lista2)
print cantRep
