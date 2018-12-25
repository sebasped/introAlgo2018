# -*- coding: utf-8 -*-

from Pila import *


def capicua(string) :

	long = len(string)
	RV = True

	# si len es 1 entonces string="#" y por lo tanto es capicúa.
	# la precondición es que el string sea no vacío.
	if long > 1:
		pila = Pila()
		i = 0

		while string[i] != "#":
			pila.apilar(string[i])
			i = i+1

		i=i+1 #para pasar el "#"

		while not pila.vacia() and i<long and string[i]==pila.tope() :
			pila.desapilar()
			i = i+1

		RV = (i==long and pila.vacia())

	return RV


string = "sdsd#dsd"
# string = "das#sad"
# string = "as#ssa"
# string = "#"
RV = capicua(string)
print RV
