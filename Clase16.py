#Iteracion y control de flujo con bucles en Python
#for

numbers = [1,2,3,4,5,6]

for i in numbers:
    print("Aqui i es igual a:", i+1)

#Iterar con coleccion de datos

for i in range(3,10):
    print(i)

#Iterar Con variable if

fruits =["Manzana", "pera", "uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

#Iterar Con variable while//Modificar la condicional para que pare el ciclo

x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1

#iterar con continue

numbers = [1,2,3,4,5,6]

for i in numbers:
    if i ==3:
        continue
    print("Aqui i es igual a:", i)