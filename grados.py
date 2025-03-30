
from os import system 
system("cls")

#2) Para el departamento de Pinturas:
  # A.	Se ingresa una temperatura en Fahrenheit y la debemos mostrar en Centígrados con un mensaje concatenado
grados_c = int(input("ingrese los grados"))
grados_farenheit= int(input("ingrese los farenheit"))
grado_f_a_c  =    ((grados_farenheit - 32) * (5/9)) 
    
   #	Se ingresa una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
grados_c_a_f=     (grados_c  * 9/5) + 32 
print (f"los grados farenheit: {grados_farenheit}\n a centigrados es: {grado_f_a_c}")
print (f"los grados centigrados: {grados_c}\n a farenheit es: {grados_c_a_f}")
