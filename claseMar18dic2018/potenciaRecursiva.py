# -*- coding: utf-8 -*-


#calcula la exponencial en forma recursiva
def potencia(nro, exp):

    RV = 0
    if exp == 0 :
        RV = 1
    else :
        RV = potencia(nro, exp-1)*nro

    return RV


res = potencia(1.1,3)
print res
