# Numero mayor y menor de una lista

# Lista donde se van a almacenar los numeros
lista = []

# Se solicita al usuario la cantidad de números que quiere ingresar, numeros enteros
cant = int(input("Cuantos números desea ingresar? "))

# Incia un contador para seguir la cantidad de números ingresados
i = 1

# Bucle while para ingresar los números solicitados por el usuario
while i <= cant:
    # El usuario que ingresa un número y se almacena en la lista
    n = int(input(f"{i} Ingrese un numero: "))
    lista.append(n)  # Se agrega el número a la lista
    i += 1  # Se incrementa el contador para el siguiente número y se detenga el bucle

# Mostramos la lista
print("Lista: ")
print(lista)

# Mostramos el numero mayor de la lista
print("Numero mayor: ", max(lista))

# Mostramos el numero menor de la lista
print("Numero menor: ", min(lista))
