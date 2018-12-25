# -*- coding: utf-8 -*-


#calcula la exponencial en forma recursiva
def suma(lista):

    RV = 0
    if len(lista) == 1 :
        RV = lista[0]
    else :
        RV = suma(lista[1:]) + lista[0]

    return RV


res = suma([1,2,3,4])
print res
