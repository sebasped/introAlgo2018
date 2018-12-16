# -*- coding: utf-8 -*-
# Convierte millas a kilómetros

import sys

millas = float(sys.argv[1])
kilometros = millas*1.6

millas, kilometros = round(millas,2), round(kilometros,2)

print millas, "millas son", kilometros, "kilómetros"
