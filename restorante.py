       
#3) Escribe un programa que pida al usuario el total de una 
# cuenta en un restaurante
#y el porcentaje de propina que desea dejar. 
#El programa debe calcular y mostrar la cantidad de propina y 
# el total a pagar
#antes y luego de la misma:
#Precio: x
#Propina: x
#Precio con propina: x

cuenta=int(input("total de la cuenta: "))
propina =cuenta*0.1
precio_con_propina=cuenta+propina
msj=""
msj+=f"el precio sin propina es: {cuenta}\n"
msj+=f"la propina es: {propina}\n"
msj+=f"el precio con propina es: {precio_con_propina}\n"
print(msj)
