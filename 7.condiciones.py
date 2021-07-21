# CONDICIONALES 

# EJEMPLOS:

# Ejemplo No.1 (Uso del if)

mi_edad = 21
edad_de_mi_hermano = 16

if(mi_edad>edad_de_mi_hermano):
    print("Yo soy más grande que mi hermano")


# Ejemplo No.2 (Uso del else)
#      (Hacer esto si es no es cierto)

mi_edad = 21
edad_de_mi_hermano = 25

if(mi_edad>edad_de_mi_hermano):
    print("Yo soy más grande que mi hermano")
else:
    print("Mi hermano es más grande que yo")


# Ejemplo No.3 (Uso del elif (Else if))
#      2da. Condición (Hacer esto si es no es cierto)

mi_edad = 21
edad_de_mi_hermano = 16

if(mi_edad>edad_de_mi_hermano):
    print("Yo soy más grande que mi hermano")
elif(edad_de_mi_hermano==mi_edad):
    print("Tenemos la misma edad")
else:
    print("Mi hermano es más grande que yo")