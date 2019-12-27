def tot_participantes ():
    tot_participantes = raw_input("ingrese la cantidad de chips repartidos: ")
    return tot_participantes
def porcentaje (cant,tot):
    porciento=cant*100/tot_participantes
    return porciento
def promedio (suma_edades,cant_que_llego):
    edad_promedio=suma_edades/cant_que_llego
    return edad_promedio
def main():
    print tot_participantes()
    cant=raw_input("ingrese la cantidad de participantes que llego: ")
    print porcentaje(cant,tot_participantes)

    
    
