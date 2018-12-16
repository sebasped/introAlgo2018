# -*- coding: utf-8 -*-

# Tabla para convertir de Fahrenheit a Celsius

def getMin(listaValores):
    cantidad = len(listaValores)
    min = listaValores[0]
    i = 1
    while i <= cantidad-1:
        if listaValores[i] < min:
            min = listaValores[i]
        i = i + 1
    return min

def getMax(listaValores):
    cantidad = len(listaValores)
    max = listaValores[0]
    i = 1
    while i <= cantidad-1:
        if listaValores[i] > max:
            max = listaValores[i]
        i = i + 1
    return max

def computeMean(listaValores):
    cantidad = len(listaValores)
    i = 0
    sumatoria = 0.0
    while i <= cantidad-1:
        sumatoria = sumatoria + listaValores[i]
        i = i + 1
    promedio = sumatoria/cantidad  #sumatoria ya es float
    return promedio

valores = [23,4,67,32,13]
print "El mínimo valor es:", getMin(valores)
print "El máximo valor es:", getMax(valores)
print "El promedio es:", computeMean(valores)
