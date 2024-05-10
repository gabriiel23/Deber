# Método de búsqueda binaria

# Definición de la función de búsqueda binaria
def busqueda_binaria(lista, elemento):
    # Inicialización de los límites izquierdo y derecho del rango de búsqueda
    izquierda, derecha = 0, len(lista) - 1
    
    # Bucle para buscar en el rango mientras el límite izquierdo sea menor o igual al límite derecho
    while izquierda <= derecha:
        # Cálculo del índice del elemento medio del rango de búsqueda
        medio = (izquierda + derecha) // 2
        
        # Compara el elemento medio con el elemento buscado
        if lista[medio] == elemento:
            return medio  # Devuelve el índice si encuentra el elemento
        elif lista[medio] < elemento:
            izquierda = medio + 1  # Ajusta el límite izquierdo si el elemento está en la mitad derecha
        else:
            derecha = medio - 1  # Ajusta el límite derecho si el elemento está en la mitad izquierda
    
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

# Realiza la búsqueda binaria del número ingresado
indice = busqueda_binaria(numeros, clave)

# Muestra el resultado de la búsqueda
if indice is not None:
    print(f"El número {clave} se encuentra en el índice {indice + 1} de la lista.")
else:
    print(f"El número {clave} no se encuentra en la lista.")
