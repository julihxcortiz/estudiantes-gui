to_do = ["dirigirnos al hotel",
       "ir a almorzar",
       "visitar un museo",
       "volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.1, True, [1,2,3]]
print(mix)
print(len(mix))

# indexacion
print("primer elemento: ", mix[0])
print("segundo elemento: ", mix[1])
print("ultimo elemento: ", mix[-1])
string="HOLA MUNDO"
# listas
print("primer elemento: ", string[0])
print("segundo elemento: ", string[1])
print("ultimo elemento: ", string[-1])
print(mix[2:-2])
# Metodos
mix.append(False)
print(mix)
mix.append (["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers_1 = [1,2,100,90,45,3,4,5]
print(numbers_1)
print("mayor: ", max(numbers_1))
print("menor: ", min(numbers_1))
del numbers_1[-1]
print(numbers_1)
del numbers_1[:2]
print(numbers_1)