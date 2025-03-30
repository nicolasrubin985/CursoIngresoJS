from os import system 
system("cls")

respuesta = "si"
nombre_mas_joven =0
edad_mas_viejo_a =0
flag_casado_mas_joven = 0
flag_mas_viejo = 0
nombre_mas_viejo=0
sexo_mas_viejo_a=0
contador_mujeres_casadas =0
contador_mujeres =0
acum_edad_mujeres = 0
acum_edad_solteros=0
contador_solteros=0
edad_casado_mas_joven=0
promedio_edad_mujeres = 0




while (respuesta == "si" ):
    nombre = input ("ingresa el nombre: ")
    edad = int(input(" ingresa la edad: "))
    while ( edad <17):
        edad = int(input("invalido, tiene que ser mayor a 18 años"))

    estado_civil = input("ingresar el estado civil: (soltero), (casado) o (viudo)")
    while (estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "viudo" ):
        estado_civil = input("invalido, ingresar soltero, casado o viudo. ")
    sexo = input("ingrese el sexo.")
    while sexo != "M" and sexo != "F":
        sexo= input("invalido ingrese F para femenino y M para masculino.")

    respuesta= input("quiere seguir ingresando si/no: ") 
    #a)    
if sexo == "M":
    if  estado_civil == "casado" and flag_casado_mas_joven == 0 :
         nombre_mas_joven = nombre
         edad_casado_mas_joven = edad
         flag_casado_mas_joven = 1
         
    if edad < edad_casado_mas_joven:
        edad_casado_mas_joven = edad 
        nombre_mas_joven = nombre
    #e)         
    if estado_civil =="soltero":
            acum_edad_solteros +=edad
            contador_solteros +=1            
            
         

    #b)
if flag_mas_viejo ==0:
        nombre_mas_viejo_a = nombre
        sexo_mas_viejo_a= sexo
        
if edad > edad_mas_viejo_a :
    edad_mas_viejo_a = edad 
    nombre_mas_viejo_a= nombre
    sexo_mas_viejo_a= sexo
    #C)
else: 
    acum_edad_mujeres += edad
    contador_mujeres += 1
if estado_civil == "casado" and estado_civil =="viudo":
    contador_mujeres_casadas += 1
#D) 
if contador_mujeres > 0:
    promedio_edad_mujeres = acum_edad_mujeres / contador_mujeres
    
promedio_solteros= acum_edad_solteros/ contador_solteros   

msj = ""
msj += (f"Nombre del casado mas joven: {nombre_mas_joven}") # punto a
msj += (f"Nombre del pasajero mas viejo/a: {nombre_mas_viejo_a} || sexo: {sexo_mas_viejo_a}") # punto b
msj += (f"cantidad de mujeres casadas o viudas: {contador_mujeres_casadas}") # punto c
msj += (f"promedio de edad que hay entre mujeres: {promedio_edad_mujeres}")
msj += (f"promedio de edad de hombres solteros: {promedio_solteros}")

print (msj)





        

        

     

        
