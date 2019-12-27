def horario_en_segundos(h,m,s):
    """toma el horario de largada del participante, dado en horas, minutos y segundos, y los pasa a segundos."""
    horario_largada_segundos=(m*60)+(h*3600)+s
    return horario_largada_segundos

def tiempo_en_hms(s):
    """toma diferentes marcas de tiempo, dadas en segundos, y las traduce en horas, minutos y segundos."""
    hm=s/3600
    mm=(s%3600)/60
    sm=(s%3600)%60
    return hm,mm,sm

def h_m_s_valida(hora,minuto,segundo):
    """Toma las horas, minutos y segundos de un horario y comprueba que sean validas"""
    while hora < 0 or hora > 24:
        hora=input ("Hora ingresada es invalida, por favor, reingrese horas: ")
    while minuto < 0 or minuto > 60:
        minuto=input ("Minuto ingresado es invalido, por favor, reingrese minutos: ")
    while segundo < 0 or segundo > 60:
        segundo=input ("Segundo ingresado es invalido, por favor, reingrese segundos: ")
    return hora,minuto,segundo

def inicio_valido(h,m,s):
    """Toma las horas, minutos y segundos del horario de inicio de la carrera, y comprueba que en conjunto, sean mayor o igual a 8 horas"""
    horario_inicio_valido=h_m_s_valida(h,m,s)
    h,m,s=horario_inicio_valido
    while h < 8 and m < 60:
        print "Error: El horario debe ser mayor a 8 horas, vuelva a introducir datos:"
        h= input ("Ingrese la hora de inicio de la carrera: ")
        m= input ("Ingrese los minutos de inicio de la carrera: ")
        s= input ("Ingrese los segundos de inicio de la carrera: ")
        horario_inicio_valido=h_m_s_valida(h,m,s)
        h,m,s=horario_inicio_valido
    return h,m,s   
    
def largada_valida((h,m,s),(h2,m2,s2)):
    """Toma las horas, minutos y segundos del horario de largada de la carrera, y comprueba que sean mayores o iguales que el de inicio"""
    horario_inicio_valido=h_m_s_valida(h,m,s)
    horario_largada_valido=h_m_s_valida(h2,m2,s2)
    h,m,s=horario_inicio_valido
    h2,m2,s2=horario_largada_valido
    horario_inicio_seg=horario_en_segundos(h,m,s)
    horario_largada_seg=horario_en_segundos(h2,m2,s2)
    while (horario_inicio_seg > horario_largada_seg):
        print "Error: El horario de largada es menor que el horario de inicio de la carrera, vuelva a ingresar"
        h2= input ("Ingrese la hora de largada de la carrera: ")
        m2= input ("Ingrese los minutos de largada de la carrera: ")
        s2= input ("Ingrese los segundos de largada de la carrera: ")
        horario_largada_valido=h_m_s_valida(h2,m2,s2)
        h2,m2,s2=horario_largada_valido
        horario_largada_seg=horario_en_segundos(h2,m2,s2)
    return h2,m2,s2

def llegada_valida((h,m,s),(h2,m2,s2)):
    """Toma las horas, minutos y segundos del horario de largada de la carrera, y comprueba que sean mayores o iguales que el de inicio"""
    horario_largada_valido=h_m_s_valida(h,m,s)
    horario_llegada_valido=h_m_s_valida(h2,m2,s2)
    h,m,s=horario_largada_valido
    h2,m2,s2=horario_llegada_valido
    horario_largada_seg=horario_en_segundos(h,m,s)
    horario_llegada_seg=horario_en_segundos(h2,m2,s2)
    while (horario_llegada_seg<horario_largada_seg+7200):
        print "Error: El horario de llegada del participante con relacion al horario de largada debe ser mayor a 2 horas, vuelva a ingresar"
        h2= input ("Ingrese la hora de llegada de la carrera: ")
        m2= input ("Ingrese los minutos de llegada de la carrera: ")
        s2= input ("Ingrese los segundos de llegada de la carrera: ")
        horario_llegada_valido=h_m_s_valida(h2,m2,s2)
        h2,m2,s2=horario_llegada_valido
        horario_llegada_seg=horario_en_segundos(h2,m2,s2)
    return h2,m2,s2        
 
def marca_tiempo(horario_largada,horario_llegada):
    """Toma el horario de largada y llegada del participante por parametro y determina su marca de tiempo"""
    h,m,s=horario_largada
    h2,m2,s2=horario_llegada
    horario_largada_seg=horario_en_segundos(h,m,s)
    horario_llegada_seg=horario_en_segundos(h2,m2,s2)
    marca_tiempo=horario_llegada_seg - horario_largada_seg
    marca_tiempo_hms=tiempo_en_hms(marca_tiempo)
    h,m,s=marca_tiempo_hms
    return h,m,s

def menor_marca_tiempo(marca_de_tiempo,menor_marca):
    """toma la marca de tiempo del participante y la menor marca de tiempo por parametro, y compara cual de las dos es la menor marca"""
    h,m,s=marca_de_tiempo
    marca_de_tiempo_seg=horario_en_segundos(h,m,s)
    h2,m2,s2=menor_marca
    menor_marca_seg=horario_en_segundos(h2,m2,s2)
    while menor_marca_seg == 0:
        menor_marca= marca_de_tiempo
        h,m,s=menor_marca
        return h,m,s
    while menor_marca_seg > 0:
        if marca_de_tiempo_seg < menor_marca_seg:
            menor_marca=marca_de_tiempo
            h,m,s=menor_marca
            return h,m,s
        else:
            h,m,s=menor_marca
            return h,m,s

def numericos_validos(valornum):
    tablanumerica=["1","2","3","4","5","6","7","8","9","0"]
    error = 1
    while error == 1:
        error = 0
        for char in valornum:
            if char not in tablanumerica:
                error = 1
        if error == 1:
            valornum = raw_input("El dato ingresado es invalido, ingrese un valor numerico: ")
    return int(valornum)
