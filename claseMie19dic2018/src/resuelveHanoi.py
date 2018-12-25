# -*- coding: utf-8 -*-

from Hanoi import *

def resuelveHanoiAux(n,desde,hacia,otra):
	if n>1:
		resuelveHanoiAux(n-1,desde,otra,hacia)
		torreHanoi.mover(desde,hacia)
		resuelveHanoiAux(n-1,otra,hacia,desde)
	else:
		torreHanoi.mover(desde,hacia)


def resuelveHanoi(n):
	resuelveHanoiAux(n,0,2,1)


n = 19 # cantidad de discos
torreHanoi = Hanoi()
for i in range(n):
	torreHanoi.poner(0,n-1-i)
# for i in range(n):
# 	print torreHanoi.tope(0)
# 	torreHanoi.sacar(0)
# for i in range(n):
# 	torreHanoi.poner(0,n-1-i)

resuelveHanoi(n)
for i in range(3):
	print torreHanoi.vacio(i)

for i in range(n):
	print torreHanoi.tope(2)
	torreHanoi.sacar(2)
