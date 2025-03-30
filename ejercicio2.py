

 ejercicio 2b
EJRCICIO1

numero = int (input("ingresar numero consecutivos del 1 al 10: "))
numeros_pares = 0
contador = 0
while contador <10: 
    if numero % 2 == 0:     
      sumar= numero + numeros_pares
      numeros_pares=sumar
      contador = contador + 1
      numero=int(input("ingrese el siguiente numero: "))
    else: 
        contador = contador + 1
        numero = int(input("ingrese el siguiente numero:"))

print("la suma de todos los nuemros pares es:",numeros_pares)

EJERCICIO2
contraseña = input(" ingrese contraseña: ")

while contraseña != "utn750": 
    contraseña =input("contraseña incorrecta, ingrese nuevamente contraseña:")

print(" contraseña correcta, bienvenido al curso de nivelacion:")
numero = int(input("ingrese un numero en el rango del 0 al 9:"))

EJERCICIO 3.

while numero < 0 or numero > 9:
    numero =int(input("fuera de rango, ingrese nuevamente:"))
print("tu numero es:", numero )

EJERCICIO 4
letra = int (input("ingrese las letras U, T o N: "))

while letra !="U" and letra !="T" and letra !="N":

    letra= input("letra incorrecta, ingrese nuevamente la letra.")

print("tu letra es:", letra )

ejercicio 5

numero = int(input(" ingrese 5 numeros: "))
contador = 0
acumulador = 0 
while contador <= 4 :
    acumulador = numero + acumulador 
    contador = contador +1 
    promedio = acumulador / 5 


print("la suma de los numeros es:", acumulador )
print("el promedio es de:", promedio )    

