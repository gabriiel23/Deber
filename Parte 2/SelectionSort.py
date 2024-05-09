# Ejercicio de Selection Sort

# Creaamos la funcion
def selectionSort(lista):
    # Creamos un rango de índices para recorrer la lista
    elementos = range(0, len(lista) - 1)
    
    # Iteramos sobre los elementos de la lista
    for i in elementos:
        # Suponemos que el valor mínimo está en la posición actual
        min_valor = i

        # Iteramos sobre los elementos restantes de la lista
        for j in range(i + 1, len(lista)):
            # Si encontramos un valor menor que el mínimo actual
            if lista[j] < lista[min_valor]:
                # Actualizamos el índice del valor mínimo
                min_valor = j

        # Si el mínimo no está en la posición actual, lo intercambiamos
        if min_valor != i:
            lista[min_valor], lista[i] = lista[i], lista[min_valor]

    # Retornamos la lista ordenada
    return lista

# Ejemplo de uso del algoritmo selection sort
print(selectionSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
