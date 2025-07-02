# Desarrolla un programa en Python que permita registrar a 3 estudiantes ingresando su nombre, edad y nota final. Luego el sistema debe calcular y mostrar:
# El promedio de las notas.
# Qué estudiantes son mayores de edad.
# Qué estudiantes aprobaron (nota mayor o igual a 3.0).
# El estudiante con la mejor nota.

# Desarrollo:

# Crear lista abierta de estudiantes

estudiantes=[]


# Crear una funcion que operara como menu para el usuario

def informacion_estudiantes():
    print("\n---informacion estudiantes---")
    print("1. Agregar datos estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Ver promedio de las notas")
    print("4. Ver estudiantes mayores de edad")
    print("5. Ver estudiantes que aprobaron")
    print("6. Ver el mejor estudiante")
    print("7. Salir")

# Defina funcion para agregar informacion de los estudiantes (nombre, edad y nota final)
# Defina que la lista abierta tenga 3 o menos estudiantes
# Solicite al usuario que ingrese nombre, edad y nota final separados por comas.
# Imprima un mensaje confirmando que la informacion ha sido agregada
# De lo contrario imprima no se puede agregar dato vacio

def data_estudiantes():
    if len(estudiantes)>=3:
        print("Ya se han registrado los 3 estudiantes")
        return
    data_entrada = input("Ingrese nombre, edad y nota final separados por comas: ")
    try:

# Separar los valores por coma

        partes= data_entrada.split(",")
        if len(partes) !=3:
            raise ValueError("Debe ingresar exactamente 3 datos.")
        
        nombre_str, edad_str, nota_str = partes

# Convertir los types al formato de manejo

        nombre= nombre_str.strip()
        edad= int(edad_str.strip())
        nota_final=float(nota_str.strip())

# Validacion nombre

        if not nombre:
            print("El nombre no puede estar vacio")
            return

# Validacion edad

        if edad<=0:
            print("La edad debe ser mayor que 0")
            return

# Validacion de nota        
        
        if not (0<= nota_final<=5):
            print("La nota debe estar entre 0 y 5")
            return

# Agregar estudiante a lista de estudiantes

        estudiantes.append([nombre, edad, nota_final])

# Mostrar al usuario  
      
        print("Nombre: ", nombre)
        print("Edad: ", edad, "Años")
        print("Nota final: ", f"{nota_final:.2f}" )
   
    except ValueError as e:
        print(f"Error en los datos {e}")


# Defina una funcion para ver los estudiantes almacenados en la lista abierta.
# Recorra la lista de estudiantes, y para cada uno muestra su posición en la lista (empezando desde 1), su nombre, su edad y su nota final con dos cifras decimales.
# Si no hay estudiantes registrados imprimir: no hay estudiantes.

def ver_estudiantes():
    if estudiantes:
        print("\n---Lista de estudiantes---")
        for i, est in enumerate(estudiantes, 1):
            print(f"{i}. Nombre: {est[0]}, Edad: {est[1]}, Nota final: {est[2]:.2f}")
    else:
        print("No hay estudiantes registrados")

# Defina una funcion para ver el promedio de las notas finales de los estudiantes.
# Si no hay estudiantes, devuelve None para indicar que no se puede calcular el resultado.
# Cree una nueva lista llamada notas que contiene solo las notas finales (est[2]) de cada estudiante registrado en la lista estudiantes.
# Calcula el promedio de notas al sumar todos los valores de la lista notas y dividir ese resultado por la cantidad total de notas registradas.
# La impresion se hace en el motor de los datos

def promedio_notas(estudiantes):
    if not estudiantes:
        return None
    notas=[est[2] for est in estudiantes]
    promedio= sum(notas) / len(notas)
    return promedio

# Defina una funcion para ver los estudiantes mayores de edad.
# Recorra la lista estudiantes y para cada estudiante obtenga su posición en la lista (empezando desde 1).
# Si la edad del estudiante (est[1]) es mayor o igual a 18, imprima su número en la lista, nombre y edad.

def estudiantes_mayores(estudiantes):
    print("\n---Estudiantes mayores de edad---")
    for i, est in enumerate(estudiantes,1):
        if est[1]>=18:
            print(f"{i}. {est[0]} - {est[1]} años")

# Defina una funcion para ver los estudiantes que aprobaron.
# Cree una nueva lista denominada aprobados donde muestre los estudiantes que tienen nota mayor o igual 3.
# Si hay aprobados recorra la lista estudiantes y para cada estudiante obtenga su posicion en la lista (empezando desde 1).
# Imprima el numeral, el nombre y la nota con 2 decimales.
# Si no imprima ningun estudiante aprobo

def estudiantes_aprobaron(estudiantes):
    print("\n---Estudiantes aprobados---")
    aprobados= [est for est in estudiantes if est[2]>=3]
    if aprobados:
            for a, est in enumerate(aprobados,1): 
                print(f" {a}.{est[0]} - Nota: {est[2]:.2f}")
    else:
        print("Ningun estudiante aprobo")

# Defina una funcion para ver la maxima nota de los 3 estudiantes.
# Si la lista estudiantes está vacía, imprima el mensaje 'No hay estudiantes registrados' y termine la ejecución de la función (usando return).
# Busque la calificacion mas alta mediante key=lambda e imprima la persona y la nota en decimal

def estudiante_max(estudiantes):
    print("\n---Mejor estudiante---")
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    else:
        mejor_nota=max(estudiantes, key=lambda est: est[2])
        print(f"{mejor_nota[0]}- Nota: {mejor_nota[2]:.2f}")
        

# Bucle principal del programa

while True:
    informacion_estudiantes()
    opcion = input("Seleccione una opcion: ")
    
    if opcion=="1":
        data_estudiantes()
    elif opcion=="2":
        ver_estudiantes()
    elif opcion=="3":
        promedio= promedio_notas(estudiantes)
        if promedio is None:
            print("No hay estudiantes registrados aun")
        else:
            print(f"Promedio de notas: {promedio:.2f}")
    elif opcion=="4":
        estudiantes_mayores(estudiantes)
    elif opcion=="5":
        estudiantes_aprobaron(estudiantes)
    elif opcion=="6":
        estudiante_max(estudiantes)
    elif opcion =="7":
        print("Gracias por visitar nuestro programa, hasta luego")
        break
    else:
        print("Opcion no valida, intente de nuevo")
        
    









