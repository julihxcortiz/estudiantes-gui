#Desarrolla un programa en Python que muestre un menú al usuario con las siguientes opciones:
#1. Agregar producto a la lista de compras.
#2. Ver productos en la lista.
#3. Eliminar un producto por nombre.
#4. Salir del programa.
#La lista debe mantenerse actualizada hasta que el usuario decida salir.

#SOLUCION:

# Crear lista global que se usará dentro de la función para acumular productos
lista_compras = []

# Mientras se cumpla la condicion true, la lista se mostrara continuamente 
while True:
    print("\n--- Lista de Compras ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Eliminar producto")
    print("4. Salir")

# Se solicita que el usuario ingrese una opcion de la lista anterior
    opcion = input("Elige una opción: ")

# Si la opcion es 1 : 
# a: solicite al usuario el nombre del producto.
# b: Agrega el producto ingresado a la lista de compras.
# c: Imprima un mensaje confirmando que el producto fue agregado.
    if opcion == "1":
        producto = input("Nombre del producto: ")
        lista_compras.append(producto)
        print(f"{producto} agregado.")

# Si la opcion es 2 :
# a: A partir de la lista de compras conformada en memoria, imprima un anuncio que diga: Productos en la lista
# b: Enumereme los productos guardados en memoria nombrando como 1 el primer item
# c: Imprima la enumeracion de los productos
# d: si no hay informacion imprima: lista vacia
    elif opcion == "2":
        if lista_compras:
            print("Productos en la lista:")
            for i, prod in enumerate(lista_compras, 1):
                print(f"{i}. {prod}")
        else:
            print("La lista está vacía.")

# si la opcion es 3:
# a: Solicite al usuario el nombre del producto que desea eliminar
# b: Si el producto esta en la lista de compras eliminelo
# c: Imprima un mensaje confirmando que el producto fue eliminado.
# d: De lo contrario imprima un mensaje mencionando que el producto no esta en lista

    elif opcion == "3":
        producto = input("Nombre del producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print(f"{producto} ha sido eliminado.")
        else:
            print(f"{producto} no está en la lista.")
# Si la opcion es 4:
# a: Imprima salir del programa y rompa el ciclo
    elif opcion == "4":
        print("Saliendo del programa...")
        break

# De ser FALSE la condicion incial imprima opcion no valida
    else:
        print("Opción no válida. Intenta de nuevo.")
