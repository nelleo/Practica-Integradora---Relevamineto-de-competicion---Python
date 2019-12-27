def edad_valida(num):
    """Sirve para validar que la edad sea mayor o igual a 18 y menor
        o igual a 65 anios"""
    while (num < 18) or (num > 65):
        num = input("La edad ingresada es invalida, por favor reingrese la edad: ")
    return num
    
    
def genero_valido(gen):
    """verifica el genero ingresado < 'm' si es masculino, 'f' si es femenino >  retorna en
       mayuscula, de lo contrario se pide volver a ingresar el genero"""
    while gen != "f" and gen != "F" and gen !="m" and gen !="M":
        gen = raw_input ("Por favor ingrese un genero valido: ")
    if gen == "f":
            gen = "F" 
    elif gen == "m":
            gen = "M"
    return gen

def inscripcion_valida():
    """La funcion recibe por teclado un numero de inscripción y verifica que sea mayor
       o igual a 0, en el caso de ser 0, pide validacion de dato"""
    n_ins = input ('Ingrese el numero de inscripcion' \
                                ' o pulse "0" para dejar de ingresar datos: ')
    sale = "N"
    while n_ins <= 0 and sale == "N" or sale == "n":
        if n_ins == 0:
            sale = raw_input("Esta seguro que desea detener la carga de datos? <S / N>: ")
            if sale == "S" or sale == "s":
                return n_ins
            elif sale == "N" or sale == "n":
                n_ins = input ('Ingrese el numero de inscripcion' \
                                ' o pulse "0" para dejar de ingresar datos: ')
        else:    
         n_ins = input("Numero invalido, vuelva a ingresar: ")
    return n_ins

        
    
            
    
