def selectionSort(lista):
	for i in range(0,len(lista)):
		posmin = i
		for j in range(i+1,len(lista)):
			if lista[j]<lista[posmin]:
				posmin = j

		temp = lista[i]
		lista[i] = lista[posmin]
		lista[posmin] = temp


def insertionSort(lista):
	for i in range(1,len(lista)):
		valor_actual = lista[i]
		pos = i
		while pos>0 and lista[pos-1]>valor_actual:
			lista[pos] = lista[pos-1]
			pos = pos-1

		lista[pos] = valor_actual

def bubbleSort(lista):
	for i in range(0,len(lista)):
		for j in range(0,len(lista)-1):
			if lista[j]>lista[j+1]:
				temp = lista[j]
				lista[j] = lista[j+1]
				lista[j+1] = temp


lista_original = [10,13,95,100,66,0,98,42,17]
lista_a_ordenar = lista_original
print "Selection Sort"
selectionSort(lista_a_ordenar)
print lista_a_ordenar

print "Insertion Sort"
insertionSort(lista_a_ordenar)
print lista_a_ordenar

print "Bubble Sort"
bubbleSort(lista_a_ordenar)
print lista_a_ordenar