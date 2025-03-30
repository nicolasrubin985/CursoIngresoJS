'''
Debemos realizar la carga de productos de prevención de contagio hasta que el usuario quiera, 
de cada una debo obtener los siguientes datos: 
el tipo (validar "barbijo" , "jabón" o "alcohol") , 
el precio (validar entre 100 y 300),
la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades), 
la Marca y el fabricante. 
Se debe Informar al usuario lo siguiente:

a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
b) Del ítem con más unidades, el fabricante 
c) Cuántas unidades de jabones hay en total
d) Porcentaje de barbijos 
e) Cual fue el tipo de producto más comprado
'''

from os import system 
system("cls")

acumjabon = 0
flag_caro_barbijo = 0
flag_unidades = 0
tipo_mas_comprado = 0
respuesta = "Si"
contador_barbijo = 0 
contador_jabon = 0
contador_alcohol = 0 
contador_general = 0
acum_barbijo = 0 
acum_alcohol = 0
while (respuesta == "Si"):
    tipo = input (" ingrese el tipo del producto: ")
    while (tipo != "barbijo" and tipo != "janbon" and tipo != "alcohol" ):
        tipo = input ("el tipo es incorrecto. tiene que ser barbijo, jabon o alcohol")
    precio = int(input (" ingrese el precio entre 100 y 300: "))
    while ( precio < 100 or precio > 300) :
        precio = int (input (" el rango del precio tiene que estar entre 100 y 300. "))
    unidades = int (input ("ingrese las unidades entre 0 y 1000"))
    while (unidades < 10 or unidades > 1000) :
        unidades = int ( input (" unidades invalidas. ingrese nuevamente. ")) 
    marca = input (" ingrese la marca: ")
    fabricante = input ("ingrese el fabricante: ")

if (tipo == " barbijo " )
    acum_barbijo = unidades
    if (flag_caro_barbijo == 0  ):
        precio_mas_caro = precio
        cantidad_unidades_mas_caro = unidades
        fabricante_mas_caro = fabricante
        flag_caro_barbijo = 1

    elif  precio > precio_mas_caro :
        precio_mas_caro = precio
        cantidad_unidades_mas_caro = unidades
        fabricante_mas_caro = fabricante    
elif tipo == "jabon" :
     acumjabon += unidades 
     contador_jabon +=1
else:
    acum_alcohol += unidades    

if flag_unidades:
     unidadesmayor = unidades 
     fabricante_con_mas_unidades = fabricante 
     tipo_mas_comprado = tipo 
     flag_unidades = 1

if unidadesmayor > unidades :
    fabricante_con_mas_unidades = fabricante 
    tipo_mas_comprado = tipo 
    
if tipo == "jabon" :
     acumjabon += unidades 
     contador_jabon +=1
    
if tipo == "alcohol":
    contador_alcohol +=1

    
    
   

    contador_general += 1 

    respuesta = input( "quiere seguir ingresando productos: si/no")
    


porcentaje = (contador_barbijo * 100 ) / contador_general 
if 

msj = ""
msj += (f"Nombre del que mas votos tuvo: {nombre_votos_mayor}") # punto a
msj += (f"Nombre del que mas votos tuvo: {nombre_votos_menor} || Edad: {edad_votos_menor}") # punto b
msj += (f"Promedio de edades: {promedio}") # punto c
msj += (f"Total de votos emitidos: {total_votos}")




