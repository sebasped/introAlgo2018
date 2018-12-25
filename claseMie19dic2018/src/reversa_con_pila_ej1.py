from Pila import *

def reversa(lista) :

	long = len(lista)

	if long > 1 :
		pila = Pila()
		i = 0

		while i < long :
			pila.apilar(lista[i])
			i = i +1

		j = 0
		while (not pila.vacia()) :
			lista[j] = pila.tope()
			pila.desapilar()
			j = j + 1


# lista = [1,2,3]
# lista = [2]
# lista = []
# lista = ['a','b']
# listaCopia = lista[:]
# reversa(listaCopia)
# print listaCopia
