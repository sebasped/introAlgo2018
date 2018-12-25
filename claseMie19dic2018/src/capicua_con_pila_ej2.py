from Pila import *
from reversa_con_pila_ej1 import *

def capicua(string) :
	# RV = False

	long = len(string)

	listaDer = []
	listaIzq = []

	pila = Pila()

	i = 0
	while i < long :
		pila.apilar(string[i])
		i = i + 1

	while pila.tope() != "#" :
		listaDer = listaDer + [pila.tope()]
		pila.desapilar()
	# print listaDer
	pila.desapilar()  # desapilo el #

	while not pila.vacia() :
		listaIzq = listaIzq + [pila.tope()]
		pila.desapilar()
	# print listaIzq

	reversa(listaDer)
	# print listaDer
	RV = (listaIzq == listaDer)

	# print RV

	return RV


# string = "assd#dsd"
# string = "das#sad"
# string = "as#ssa"
string = "#"
RV = capicua(string)
print RV
