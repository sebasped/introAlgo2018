# -*- coding: utf-8 -*-

# Tabla para convertir de Fahrenheit a Celsius de 0 a 100, de a 10

fah = 0

while fah <= 100 :
    cel = (5*(float(fah)-32))/9
    print fah, "Fahrenheit son", round(cel,2), "Celsius"
    fah = fah + 10
