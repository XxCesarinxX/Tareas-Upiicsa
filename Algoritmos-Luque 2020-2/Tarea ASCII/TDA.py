import numpy
import pandas as pd

datos = [] #creamos una lista  vacia
with open("ASCII.txt", encoding="utf8") as fname: 
	lineas = fname.readlines() #cada linea es un elemento de la lista
	for linea in lineas: # bucle para quitar el espacio leido de la lista 
		datos.append(linea.strip('\n')) #una vez limpio lo agrgamos a la lista datos
#print (datos) #Se imprime la lista
mitad = len(datos) //2
conjunto_A = datos[:mitad]
conjunto_B = datos[mitad:]
