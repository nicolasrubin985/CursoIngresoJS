#La municipalidad de la ciudad está realizando un estudio de mercado para determinar cuál
#será la nueva actividad recreativa que se difundirá. Las posibles actividades son las
#siguientes: Clases de Yoga, Cine al Aire Libre, Taller de Pintura.
#Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
#propósito de conocer cuáles son las preferencias de los encuestados (no se sabe cuántos):
#Se ingresa de cada encuestado:
#● Nombre
#● Edad (no menor a 18)
#● Está jubilado (si-no)
#● Género (Masculino - Femenino - Otro)
#● Voto (YOGA, CINE, PINTURA)
#Se necesita saber:
#1. Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
#esté entre 25 y 50 años inclusive.
#2. Nombre y voto del encuestado de género Masculino con menor edad.
#3. Porcentaje de votos de cada género.
#4. Promedio de edad de los encuestados de género Femenino que votaron PINTURA.
#5. Determinar cuál fue el género que tuvo más encuestados.


respuesta="si"
cont_no_jubilados=0
flag_M_menor_edad=0
no_hay_hombres=0
no_hay_mujeres = 0

cont_pintura=0
cont_M = 0
cont_F = 0
cont_otro = 0
acum_edad_pintura = 0
while respuesta=="si":
    nombre=input("ingrese su nombre: ")
    edad=int(input("iungrese la edad mayor a 18: "))
    while (edad< 18):
        edad=int(input("edad invalida, tiene que ser mayor a 18."))
    estado=input("ingrese si es jubilado (si) (no)")
    while(estado !="si" and estado!="no"):
        estado=input("estado invalido. ingrese si/no")
    genero=input("ingrese su genero: M(masculino) F(femenino) otro")
    while(genero != "M" and genero!= "F" and genero!= "otro"):
        genero=input("invalido. ingrese M/F/otro")
    voto=input("ingrese su voto:(yoga)(cine)(pintura)")
    while(voto !="yoga"and voto != "cine" and voto!="pintura"):
        voto= input("invalido ingrese yoga cine o pintura") 
    
#1)     
    if estado=="no" and ( voto=="cine"or voto=="pintura") and (edad >24 and edad<51):
        cont_no_jubilados +=1
    respuesta= input("quiere seguir ingresando si/no: ")
#2)        
    if genero=="M":
        no_hay_hombres =1
        cont_M+=1
        if flag_M_menor_edad==0:
            edad_M_m_edad=edad
            nombre_M_m_edad=nombre
            voto_M_m_edad=voto
            flag_M_menor_edad =1
        if edad<edad_M_m_edad:
            nombre_M_m_edad=nombre
            voto_M_m_edad=voto
    elif genero =="F":
        cont_F +=1
#4)
        if  voto=="pintura" :
            cont_pintura +=1
            acum_edad_pintura += edad
    else:
        cont_otro +=1

    respuesta= input("quiere seguir ingresando si/no: ")

#3)
 
porc_M=(cont_M)*100 / (cont_M+cont_F+cont_otro)

porc_F=(cont_F)*100 /(cont_M+cont_F+cont_otro)

porc_otro=(cont_otro) *100/(cont_M+cont_F+cont_otro)

##4)



#5)
mas_encuestado="otro"
if cont_M > cont_F and cont_M > cont_F :
    mas_encuestado = ("el genero mas encuestado es: Masculino")

elif  cont_F > cont_otro :
    mas_encuestado = ("el genero mas encuestado es: Femenino")
   

msj = ""
msj += (f"Cantidad de encuestados no jubilados: {cont_no_jubilados}") # punto a
if  no_hay_hombres == 0:
    print ("no hay hombres ")
else: 
    msj += (f"Nombre del encuestado de género Masculino con menor edad {nombre_M_m_edad} || voto: {voto_M_m_edad}") # punto b

msj += (f"Porcentaje de votos de cada género: Masculino{prom_M} femenino{prom_F} otro{prom_otro} ") # punto c

if no_hay_mujeres == 0:
    print("no hay mujeres ")
      
else:
    if cont_pintura != 0 :
        prom_edad_pintura = acum_edad_pintura = cont_pintura    
    msj += (f"Promedio de edad de los encuestados de género Femenino que votaron PINTURA:  {prom_edad_pintura}")
msj += (f"promedio de edad de hombres solteros: {mas_encuestado}")

print (msj)     



