def porcentaje_participantes_llego(cant_que_llego,total_participantes):
    """calcula del total de participantes el porcentaje de partcipantes que llego"""
    porcentaje_que_llego=cant_que_llego*100.0/total_participantes
    return porcentaje_que_llego
        
def promedio_edad (suma_edades,cant_que_llego):
    """calcula de la cantidad de llegadores el promedio de sus edades"""
    if cant_que_llego > 0 :
        promedio=suma_edades*1.0/cant_que_llego
        return promedio
    else:
        return 0
def ganadores(lista,menor_marca):
    lista_ganadores=[]
    for elem in lista:
        if elem[0]==menor_marca:
         lista_ganadores.append(elem[1])
         lista_ganadores.append(elem[2])
         lista_ganadores.append(elem[3])
    return lista_ganadores



