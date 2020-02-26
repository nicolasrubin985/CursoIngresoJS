function mostrar()
{

var repeticiones = parseInt(prompt("ingrese el número de repeticiones"));

while(isNaN(repeticiones)|| repeticiones<0)
{
    repeticiones=prompt("no es un dato valido. ingresar de nuevo");

}

for (var contador=0;contador<repeticiones;contador++){

console.log("hola UTN- FRA"+ contador);
}

}//FIN DE LA FUNCIÓN