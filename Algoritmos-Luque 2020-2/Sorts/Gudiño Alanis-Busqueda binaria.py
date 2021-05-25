#busqueda binaria
numeros = [2,4,6,8,10,12,14,16,18,20]

#bucamos el punto medio

def busqueda_binaria(valor):
    inicio = 0
    fin = len(numeros) - 1
    while inicio <= fin:
        puntero = (inicio + fin) // 2
        if valor == numeros[puntero]:
            return puntero
        elif valor > numeros[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero -1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El numero {valor} no se encontro"
    else:
        return f"El numero {valor} se encuentra en la pocision {res_busqueda}"

print(buscar_valor(16))