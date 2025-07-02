#Desarrolla un programa en Python que muestre un menú al usuario con las siguientes opciones:
#1. Agregar producto a la lista de compras.
#2. Ver productos en la lista.
#3. Eliminar un producto por nombre.
#4. Salir del programa.
#La lista debe mantenerse actualizada hasta que el usuario decida salir.

#Solucion

Lista_compras = []

# Crear lista global que se usará dentro de la función para acumular productos
def mostrar_lista():
    print("\n--- Lista de Compras ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Eliminar producto")
    print("4. Salir")

# a: definir funcion para agregar producto
# b: solicite al usuario el nombre del producto.
# c: Agrega el producto ingresado a la lista de compras.
# d: Imprima un mensaje confirmando que el producto fue agregado.
# e: De lo contrario imprima no se puede agregar producto vacio

def agregar_producto():
    producto=input("ingrese el nombre del producto: ")
    if producto:
        Lista_compras.append(producto)
        print(f"{producto} agregado")
    else:
        print("no se puede agregar un producto vacio")

# a: definir funcion para ver productos
# b: A partir de la lista de compras conformada en memoria, imprima un anuncio que diga: Productos en la lista
# c: Enumereme los productos guardados en memoria nombrando como 1 el primer item
# d: Imprima la enumeracion de los productos
# e: si no hay informacion imprima: lista vacia

def ver_productos():
    if Lista_compras:
        print("productos en la lista")
        for i, prod in enumerate(Lista_compras,1):
            print(f"{i}. {prod}")
    else:
        print("la lista esta vacia")

# a: definir funcion para eliminar productos
# b: Solicite al usuario el nombre del producto que desea eliminar
# c: Si el producto esta en la lista de compras eliminelo
# d: Imprima un mensaje confirmando que el producto fue eliminado.
# e: De lo contrario imprima un mensaje mencionando que el producto no esta en lista

def eliminar_productos():
    producto= input("Nombre el producto a eliminar: ")
    if producto in Lista_compras:
        Lista_compras.remove(producto)
        print(f"'{producto}' ha sido eliminado")
    else:
        print(f"'{producto}' El producto no se encuentra en lista")

# Bucle principal del programa
while True:
    mostrar_lista()
    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        eliminar_productos()
    elif opcion == "4":
        print("¡Gracias por usar el programa! Hasta luego.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")




    

