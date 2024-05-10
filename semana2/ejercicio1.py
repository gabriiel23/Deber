# Método de búsqueda secuencial

# Definición de la función de búsqueda secuencial
def busqueda_secuencial(lista, elemento):
    # Itera sobre cada índice de la lista
    for i in range(len(lista)):
        # Compara el elemento actual con el elemento buscado
        if lista[i] == elemento:
            return i  # Devuelve el índice si encuentra el elemento
    return None  # Devuelve None si no encuentra el elemento

# Lista para almacenar los números ingresados por el usuario
numeros = []

# Solicita al usuario que ingrese 20 números y los guarda en la lista
print("Ingrese 20 elementos numéricos:")
for i in range(20):
    elemento = float(input(f"Ingrese el elemento {i + 1}: ")) 
    numeros.append(elemento)

# Función de ordenación por selección
def selectionSort(numeros):
    # Genera una secuencia de índices para recorrer la lista
    elementos = range(0, len(numeros) - 1)
    
    # Algoritmo de ordenación por selección
    for i in elementos:
        min_valor = i

        # Encuentra el índice del mínimo valor en el resto de la lista
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[min_valor]:
                min_valor = j

        # Intercambia el valor mínimo con el valor en la posición actual
        if min_valor != i:
            numeros[min_valor], numeros[i] = numeros[i], numeros[min_valor]

    return numeros

# Muestra la lista ordenada
print("La lista ordenada es la siguiente: ")
print(selectionSort(numeros))

# Solicita al usuario que ingrese un número para buscar en la lista
clave = float(input("Ingrese un número para buscar en la lista: "))

# Realiza la búsqueda secuencial del número ingresado
indice = busqueda_secuencial(numeros, clave)

# Muestra el resultado de la búsqueda
if indice is not None:
    print(f"El número {clave} SI se encuentra en el índice {indice + 1} de la lista.")
else:
    print(f"El número {clave} NO se encuentra en la lista.")
