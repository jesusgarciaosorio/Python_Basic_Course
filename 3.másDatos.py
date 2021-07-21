# Datos en forma de lista
# (usados principalmente para incluir a a más de 1 Tipo de Datos)

# EJEMPLOS

# Ejemplo No.1_Para saber que clase es nuestra lista 

lista=[1, True, 3.5, "Hola"]
print(type(lista))


# Ejemplo No.2_Para conocer el indice de valor de cada uno de nuestras listas
# Conociendo que desde el inicio de la lista empieza con el indíce: 0 seguido de 1 y así sucecivamente
 
lista=[1, True, 3.5, "Hola"]
print(lista[3])


# Ejemplo No.3_Eliminar los valores de las listas 

lista=[1, True, 3.5, "Hola"]
lista.pop()
print(lista)


# Ejemplo No.4_Agregar valores Nuevos a nuestras listas 

lista=[1, True, 3.5, "Hola"]
lista.append("Nuevo  Valor")
print(lista)

lista.insert(1, 63) # Está opción para insertarlo en en un Indíce de un valor indicado
print(lista)


# Ejemplo No.5_Para borrar los valores de nuestra lista

lista=[1, True, 3.5, "Hola"]
lista.append("Nuevo  Valor")
print(lista)

lista.clear #Función para borrar nuestros valores de la lista
print(lista)