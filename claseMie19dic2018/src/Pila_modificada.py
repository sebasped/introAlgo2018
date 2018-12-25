class PilaModificada:

	def __init__(self,x):
		self.pila = []
		self.pila.append(x)
	def apilar(self, x):
		self.pila.append(x)

	def vacia(self):
		return len(self.pila) == 0

	def tope(self):
		return self.pila[len(self.pila)-1]

	def desapilar(self):
		self.pila.pop()

pila = PilaModificada(3)
print pila
