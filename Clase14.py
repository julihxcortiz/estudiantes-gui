numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information ={"nombre": "julian",
              "apellido": "Ortiz",
              "Altura": 1.70,
              "Edad": 29}

print(information)

for key in ["Edad","Altura"]:
    del information[key]

print(information)
claves=information.keys()
print(claves)
#print(type(claves))
values= information.values()
print(values)
pairs= information.items()
print(pairs)

contacts ={"Julian": {"apellido": "Ortiz",
              "Altura": 1.70,
              "Edad": 29},"Felipe":
              {"apellido": "Fontecha",
              "Altura": 1.40,
              "Edad": 39}}

print(contacts["Felipe"])

