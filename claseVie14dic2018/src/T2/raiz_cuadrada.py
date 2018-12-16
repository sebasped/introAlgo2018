#!/usr/bin/python

def raiz_cuadrada(n):
   i = 1
   while i * i <= n:
      i = i + 1
   return i - 1

x = 1
while x <= 5:
   print raiz_cuadrada(x)
   x = x + 1

