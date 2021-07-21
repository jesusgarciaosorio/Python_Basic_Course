# USO DE LAS OPERACIONES LÓGICAS 

Nombre_de_Usuario = "Iván"
Contraseña_de_Usuario = "1235754"

if(Nombre_de_Usuario=="Iván" and Contraseña_de_Usuario=="123"):
    print("Bienvenido")
else:
    print("Error de Ingreso")



tipo_de_usuario = "administrador"
if(tipo_de_usuario == "administrador" or tipo_de_usuario == "co-administrador"):
    print("Eres un admin")
else:
    print("Eres un invitado")



print(not True) # Si la condición es True cambiala a False
