contador = 0 
min_votos = float(" inf")
max_votos = float("-inf")
acumulador_votos = 0
acumulador_edad = 0

while contador <3:
    nombre = input("ingresar nombre")

    edad= int(input("ingresar edad del competidor:"))

    while edad < 25:
        edad = int (input("la edad tiene que ser mayor a 25"))

    votos = int (input(" ingresar los votos"))

    contador +=1
    acumulador_votos = votos + acumulador_votos
    acumulador_edad = edad + acumulador_edad
promedio = acumulador_edad / contador

if votos> max_votos:
    max_votos=votos
    max_votos_nombre= nombre
if votos<min_votos:
    min_votos=votos
    min_votos_nombre = nombre 
    min_edad = edad   

print (" el competidor con mas votos es" , max_votos_nombre)
print("el candidato con menos votos es: ", min_votos_nombre, " con una edad de: ", min_edad)
print ("el promedio de edades es:", promedio )
print("el total de  votos es: ",acumulador_votos)       


from os import system 
system("cls")

'''
De los 10 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) 
que recibió en la etapa de votos

Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()
'''

flag_votos = True
suma_edades = 0
total_votos = 0
contador_jugadores = 0

while (contador_jugadores < 3):
    nombre = input("Nombre: ")

    edad = int(input("Edad: ")) 
    while (edad < 25):
        print("INVALIDA")
        edad = int(input("Edad: ")) 

    votos = int(input("Cant. votos: ")) 
    while(votos < 0):
        print("INVALIDA")
        votos = int(input("Cant. votos: ")) 

    # a. nombre del candidato con más votos
    # b. nombre y edad del candidato con menos votos
    if (flag_votos):
        flag_votos = False
        votos_mayor = votos
        votos_menor = votos

        nombre_votos_mayor = nombre
        nombre_votos_menor = nombre
        edad_votos_menor = edad

    if (votos > votos_mayor):
        votos_mayor = votos
        nombre_votos_mayor = nombre
    elif (votos < votos_menor):
        votos_menor = votos
        nombre_votos_menor = nombre
        edad_votos_menor = edad

    # c. el promedio de edades de los candidatos
    suma_edades += edad

    # d. total de votos emitidos.
    total_votos += votos

    contador_jugadores += 1

promedio = suma_edades / contador_jugadores

msj = ""
msj += (f"Nombre del que mas votos tuvo: {nombre_votos_mayor}") # punto a
msj += (f"Nombre del que mas votos tuvo: {nombre_votos_menor} || Edad: {edad_votos_menor}") # punto b
msj += (f"Promedio de edades: {promedio}") # punto c
msj += (f"Total de votos emitidos: {total_votos}") # punto d

print(msj)



    

