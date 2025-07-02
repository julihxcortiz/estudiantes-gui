# Copiar listas en python sin compartir memoria con slicing
a= [1,2,3,4,5]
b=a
print (a)
print (b)
del a[0]
print(id(a))
print(id(b))
c=a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(c)
print(a)
print(b)