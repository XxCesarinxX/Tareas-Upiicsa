datos = [] #creamos una lista  vacia
with open("ASCII.txt", encoding="utf8") as fname: 
	lineas = fname.readlines() #cada linea es un elemento de la lista
	for linea in lineas: # bucle para quitar el espacio leido de la lista 
		datos.append(linea.strip('\n')) #una vez limpio lo agrgamos a la lista datos
#print (datos) #Se imprime la lista
mitad = len(datos) //2
conjunto_A = datos[:mitad]
conjunto_B = datos[mitad:]
print("""
1.- Basear un conjunto 
2.- Que el usuario capture los enunciados de un elemento 
3.- La intercepcion de 2  conjuntos
4.- La union de 2 conjuntos
5.- la union exclusiva de 2 conjuntos 
6.- El complemento de un conjunto 
7.- La diferencia de 2 conjuntos
8.- Desplegar a pantalla los elementos de un conjunto 
9.- preguntar si 2 conjuntos son iguales 
10.- Preguntar el tamano de un conjunto (cardinalidad) 
11.- Convertir todas las letras minusculas a mayusculas 
""") 
op = int(input('Que desea hacer?'))
if op == 1:
	basea=input('Cual conjunto quiere basear 1 o 2 ?\n-->')
	if basea == 1:
		print (conjunto_A)
	else:
		print(conjunto_B)

if op == 2:
	capturar = int(input('cuantos elementos desea capturar?\n\t-->'))
	elemtos = []
	base = range(0, capturar)
	for x in base:
		buscar=input(f"{x+1}.- elemento: ")
		elemtos.append(buscar)  
	print(elemtos)		

if op == 3:
	print(conjunto_A - conjunto_B)

if op == 4:
	print('hola')

if op == 5:
	print('hola')

if op == 6:
	print('hola')

if op == 7:
	print('hola')

if op == 8:
	print('hola')

if op == 9:
	print('hola')

if op == 10:
	print('hola')

if op == 11:
	print('hola')