def apellido_valido():
    if apellido == " ":
        print "error:no a ingresado un apellido"
        apellido= raw_input("Ingrese el apellido: ")
    return apellido
    

def nombre_valido():
    if nombre == " ":
        print "error:no a ingresado un nombre"
        nombre= raw_input("Ingrese el nombre: ")
    return nombre

def edad_valida():
    if edad == " ":
        print "error:no a ingresado una edad"
        edad= input("Ingrese la edad: ")
    return edad

def genero_valido():
    if genero == " ":
        print "error:no a ingresado un genero"
        genero= raw_input("Ingrese el generoo: ")
    return genero
  
