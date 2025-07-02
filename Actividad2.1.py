#Desarrolla un programa en Python que permita registrar a 3 estudiantes ingresando su nombre, edad y nota final. Luego el sistema debe calcular y mostrar:
#El promedio de las notas.
#Qué estudiantes son mayores de edad.
#Qué estudiantes aprobaron (nota mayor o igual a 3.0).
#El estudiante con la mejor nota.

#Crear lista abierta de estudiantes

estudiantes=[]


# Crear lista global que se usará dentro de la función para recolectar informacion de los estudiantes

def informacion_estudiantes():
    print("\n---informacion estudiantes---")
    print("1. Agregar datos estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Ver promedio de las notas")
    print("4. Ver estudiantes mayores de edad")
    print("5. Ver estudiantes que aprobaron")
    print("6. Ver el mejor estudiante")
    print("7. Salir")

# a: definir funcion para agregar informacion de los estudiantes (nombre, edad y nota final)
# b: solicite al usuario que ingrese nombre, edad y nota final separados por comas.
# d: Imprima un mensaje confirmando que la informacion ha sido agregada
# e: De lo contrario imprima no se puede agregar dato vacio

def data_estudiantes():
    data_entrada = input("Ingrese nombre, edad y nota final separados por comas: ")
    try:
# Separar los valores por coma
        partes= data_entrada.split(",")
        if len(partes) !=3:
            raise ValueError("Debe ingresar exactamente 3 datos.")
        
        nombre_str, edad_str, nota_str = partes

#Convertit los types a su formato correcto
        nombre= nombre_str.strip()
        edad= int(edad_str.strip())
        nota_final=float(nota_str.strip())
#Agregar estudiante a lista de estudiantes e imprimir
        estudiantes.append([nombre, edad, nota_final])
#Mostrar al usuario        
        print("Nombre: ", nombre)
        print("Edad: ", edad)
        print("Nota final: ", nota_final )
   
    except ValueError as e:
        print(f"Error en los datos {e}")

def ver_estudiantes():
    if estudiantes:
        print("\n---Lista de estudiantes---")
        for i, est in enumerate(estudiantes, 1):
            print(f"{i}. Nombre: {est[0]}, Edad: {est[1]}, Nota final: {est[2]}")
    else:
        print("No hay estudaintes registrados")

def promedio_notas(estudiantes):
    if not estudiantes:
        return None
    notas=[est[2] for est in estudiantes]
    promedio= sum(notas) / len(notas)
    return promedio

              

def estudiantes_mayores(estudiantes):
    print("\n---estudiantes mayores de edad---")
    for i, est in enumerate(estudiantes,1):
        if est[1]>=18:
            print(f"{i}. {est[0]} - {est[1]} años")


def estudiantes_aprobaron(estudiantes):
    print("\n---estudiantes aprobados---")
    aprobados= [est for est in estudiantes if est[2]>=3]
    if aprobados:
            for a, est in enumerate(aprobados,1): 
                print(f" {a}.{est[0]} - Nota: {est[2]}")
    else:
        print("Ningun estudiante aprobo")

def estudiante_max(estudiantes):
    print("\n---Mejor estudiante---")
    for est in est[2]:
        print(max(est[2]))






# Bucle principal del programa

while True:
    informacion_estudiantes()
    opcion = input("seleccione una opcion: ")
    
    if opcion=="1":
        data_estudiantes()
    elif opcion=="2":
        ver_estudiantes()
    elif opcion=="3":
        promedio= promedio_notas(estudiantes)
        if promedio is None:
            print("No hay estudiantes registrados aun")
        else:
            print(f"promedio de notas: {promedio:.2f}")
    elif opcion=="4":
        estudiantes_mayores(estudiantes)
    elif opcion=="5":
        estudiantes_aprobaron(estudiantes)
    elif opcion=="6":
        estudiante_max(estudiantes)









