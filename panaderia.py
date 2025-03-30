#Una panadería vende barras de pan a 3.49$ cada una.
#El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas
#que no son del día. 
#Después el programa debe mostrar el precio habitual de
#una barra de pan, el descuento que se 

from os import system 
system("cls")

rta="si"
cont_barra_viejo=0
cont_barra_fresco =0


while rta =="si":
    pan=input("que pan desea: fresco/viejo: ")
    while pan!="fresco" and pan!="viejo":
        pan=input("invalida. ingrese (fresco) (viejo)")
    precio_p_fresco=3.49    
    if  pan == "fresco" :
        cont_barra_fresco += 1
    else: 
        precio_p_viejo= 3.49 * 0.6
        cont_barra_viejo +=1
    rta = input("quiere seguir comprando? si") 
    while rta != "si" and rta != "no":
        rta = input ("invalido, ingrese  si/no: ")   



msj= ""
msj+=f"barras vendidas que no son del dia: {cont_barra_viejo}""\n"
msj+=f"precio de pan fresco: {precio_p_fresco} \n descuento {precio_p_viejo}"

print(msj)