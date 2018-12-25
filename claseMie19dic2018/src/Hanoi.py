from Pila import *

class Hanoi:

	def __init__(self):
		palo1 = Pila()
		palo2 = Pila()
		palo3 = Pila()
		self.hanoi = [palo1,palo2,palo3]

	# self.hanoi[i] es una Pila

	def tope(self,palo):
		return self.hanoi[palo].tope()

	def poner(self,palo,disco):
		if (self.hanoi[palo].vacia() or self.hanoi[palo].tope() > disco):
			self.hanoi[palo].apilar(disco)
		else:
			print "Movimiento prohibido"

	def vacio(self,palo):
		return self.hanoi[palo].vacia()

	def mover(self,paloDesde,paloHasta):
		if (self.hanoi[paloHasta].vacia() or self.hanoi[paloHasta].tope() > self.hanoi[paloDesde].tope()):
			self.hanoi[paloHasta].apilar(self.hanoi[paloDesde].tope())
			self.hanoi[paloDesde].desapilar()
		else:
			print "Movimiento prohibido"

	def sacar(self,palo):
		self.hanoi[palo].desapilar()
