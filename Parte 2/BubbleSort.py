# Ejercicio del Bubble Sort

# Creamos la funcion
def bubble(lista):
    # Calculamos el índice máximo del array
    elementos = len(lista) - 1
    # Variable para controlar si la lista está ordenada o no
    orden = False

    # Mientras la lista no esté ordenada
    while not orden:
        # Suponemos que la lista está ordenada
        orden = True
        # Iteramos sobre los elementos de la lista
        for i in range(0, elementos):
            # Si el elemento actual es mayor que el siguiente
            if lista[i] > lista[i+1]:
                # Marcamos que la lista no está ordenada
                orden = False
                # Intercambiamos los elementos para ordenarlos
                lista[i], lista[i+1] = lista[i+1], lista[i]
    # Retornamos la lista ordenada
    return lista

# Ejemplo de uso del algoritmo bubble sort
print(bubble([3, 5, 1, 2, 9, 7, 4, 8, 6]))
