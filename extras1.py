#Uso de la coma en print
print("Nunca", "pares", "de", "aprender")
print("Nunca" + "pares" + "de" + "aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")
#Uso de sep
print("Nunca", "pares", "de", "aprender", sep=", ")
# Uso de end
print("Nunca", end=" ")
print("pares de aprender")
#Impresión de variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)
#Uso de formato con f-strings
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")
#Uso de formato con format
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))
#Impresión con formato específico
valor = 3.14159
print("Valor: {:.2f}".format(valor))
#Saltos de línea y caracteres especiales
print("Hola\nmundo")
#Texto con comillas
print('Hola soy \'Carli\'')
