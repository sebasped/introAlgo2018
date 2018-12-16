# -*- coding: utf-8 -*-

# Tabla para convertir de Fahrenheit a Celsius

def tabla_fahrenheit_a_celsius(fahInicial, fahFinal, paso):
    fah = fahInicial
    while fah <= fahFinal :
        cel = (5*(float(fah)-32))/9
        print fah, "Fahrenheit son", round(cel,2), "Celsius"
        fah = fah + paso

tabla_fahrenheit_a_celsius(0,100,10)
tabla_fahrenheit_a_celsius(101,110,1)
