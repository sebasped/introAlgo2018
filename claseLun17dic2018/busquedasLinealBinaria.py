# -*- coding: utf-8 -*-


def busquedaLineal(x,lista):
    esta = False
    pos = -1
    longitud = len(lista)
    j = 0

    while j < longitud:
        if lista[j] == x:
            esta = True
            pos = j
        j = j +1

    return esta, pos


def busquedaBinaria(x,lista): #supone que la lista está ordenada
    esta = False
    pos = -1
    longitud = len(lista)
    izq = 0
    der = longitud-1

    while izq < der:
        med = (izq+der)/2  #funciona igual si hace división entera
        if lista[med] < x:
            izq = med +1
        else:
             der = med

    if lista[izq] == x:
        esta = True
        pos = izq

    return esta, pos


l1 = [13, 5, 56, 16, 8]
l2 = [5, 8, 13, 16, 45, 98]

esta, pos = busquedaLineal(16,l1)
print esta, pos
esta, pos = busquedaBinaria(8,l2)
print esta, pos
