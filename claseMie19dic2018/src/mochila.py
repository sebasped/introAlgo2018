# -*- coding: utf-8 -*-

def mochila(i,pesoMax):
	valorMax = 0
	for i in range(n):
		if pesos[i] <= pesoMax:
			valor = mochila(i,pesoMax-pesos[i])
			valorAux = valores[i] + valor
			if valorMax < valorAux:
				valorMax = valorAux

	return valorMax


pesos = [12, 2, 1, 1, 4]
valores = [4, 2, 2, 1, 10]
pesoMax = 15
n=len(pesos)

max = mochila(0,pesoMax)
print max
# print cant
