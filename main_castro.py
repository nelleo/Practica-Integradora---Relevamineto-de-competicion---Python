from dominguez import h_m_s_valida,largada_valida,llegada_valida,marca_tiempo
from dominguez import menor_marca_tiempo,inicio_valido
from castro import porcentaje_participantes_llego,promedio_edad 

#Tener en cuenta que el promedio de edad no es division exacta (castro py)
#Tener en cuanta la cant que llega (Ver si es necesario)
#ejecutar pruebas completas con los 3 casos.


def main():
    total_participantes = input ("Ingrese la cantidad total de chips entregados: ")
    h_inicio= input ("Ingrese la hora de inicio de la carrera: ")
    m_inicio= input ("Ingrese los minutos de inicio de la carrera: ")
    s_inicio= input ("Ingrese los segundos de inicio de la carrera: ")
    h_inicio, m_inicio, s_inicio = h_m_s_valida(h_inicio,m_inicio,s_inicio)
    hora_inicio = inicio_valido(h_inicio, m_inicio, s_inicio)
    numero_inscripcion = 1
    cant_que_llego = 0
    suma_edades = 0
    menor_tiempo_total = (0,0,0)
    while numero_inscripcion > 0 :
        apellido = raw_input ("Ingrese el apellido: ")
        primer_nombre = raw_input ("Ingrese el primer nombre: ")
        edad = input ("Ingrese la edad: ")
        genero = raw_input ('Ingrese el genero "F" para femenino, o "M" para masculino: ')
        h_largada = input ("Ingrese la hora de largada de la carrera: ")
        m_largada = input ("Ingrese los minutos de largada de la carrera: ")
        s_largada = input ("Ingrese los segundos de largada de la carrera: ")
        hora_largada = (h_largada,m_largada,s_largada)
        largada_validada = largada_valida(hora_inicio,hora_largada)
        h_llegada = input ("Ingrese la hora de llegada de la carrera: ")
        m_llegada = input ("Ingrese los minutos de llegada de la carrera: ")
        s_llegada = input ("Ingrese los segundos de llegada de la carrera: ")
        hora_llegada = (h_llegada,m_llegada,s_llegada)
        llegada_validada = llegada_valida(largada_validada,hora_llegada)
        marca_tiempo_competidor = marca_tiempo(largada_validada, llegada_validada)
        h_marca,m_marca,s_marca = marca_tiempo_competidor
        menor_tiempo_total = menor_marca_tiempo(marca_tiempo_competidor,menor_tiempo_total)
        h_menor_marca,m_menor_marca,s_menor_marca = menor_tiempo_total
        cant_que_llego = cant_que_llego + 1
        suma_edades = suma_edades + edad
        print "\nApellido: ",apellido, \
              "\nPrimer nombre: ",primer_nombre, "\nEdad: ",edad, "\nGenero :",genero, \
              "\nHorario de largada: ",largada_validada[0],":",largada_validada[1],":",largada_validada[2],  \
              "\nHorario de llegada: ",llegada_validada[0],":",llegada_validada[1],":",llegada_validada[2],  \
              "\nMarca de tiempo: ",h_marca,":",m_marca,":",s_marca
        numero_inscripcion = input ("Ingrese num inscrip: ")
    porcentaje_llego = porcentaje_participantes_llego(cant_que_llego,total_participantes)
    edad_promedio = promedio_edad(suma_edades,cant_que_llego)
    h_menor_marca,m_menor_marca,s_menor_marca = menor_tiempo_total
    print "Menor marca de tiempo de la carrera: ",h_menor_marca,m_menor_marca,s_menor_marca, \
          "\nNumero de Participantes: ",total_participantes, \
          "\nPorcentaje de participantes que termino la carrera: ",porcentaje_llego,"%",\
          "\nPromedio de edad de participantes que completo la carrera: ",edad_promedio
                
