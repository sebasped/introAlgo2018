# -*- coding: utf-8 -*-

# Tabla para convertir de Fahrenheit a Celsius

def fahrenheit_a_celsius(fah):
    cel = (5*(float(fah)-32))/9
    return cel

def tabla_fahrenheit_a_celsius(fahInicial, fahFinal, paso):
    fah = fahInicial
    while fah <= fahFinal :
        cel = fahrenheit_a_celsius(fah)
        print fah, "Fahrenheit son", round(cel,2), "Celsius"
        fah = fah + paso

tabla_fahrenheit_a_celsius(0,100,10)
tabla_fahrenheit_a_celsius(101,110,1)
