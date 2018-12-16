#!/usr/bin/python

def imprimir_fila(fil):
   col = 1
   while col <= fil:
      print col,
      col = col + 1
   print

fil = 1
while fil <= 5:
   imprimir_fila(fil)
   fil = fil + 1

print

fil = 5
while fil >= 1:
   imprimir_fila(fil)
   fil = fil - 1

print

fil = 5
while fil >= 1:
   if fil % 2 != 0:
      imprimir_fila(fil)
      imprimir_fila(fil)
   fil = fil - 1

