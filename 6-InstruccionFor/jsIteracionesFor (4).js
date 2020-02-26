function mostrar()
{

    var repeticiones = parseInt(prompt("ingrese el número de repeticiones"));

    while(isNaN(repeticiones)|| repeticiones<0)
    {
        repeticiones=prompt("no es un dato valido. ingresar de nuevo");
    
    }
    for(var contador=0;repeticiones<1000000;contador++){

        console.log("El numero es "+contador);
        if (contador == 5){
        break;
    }
}
    


}//FIN DE LA FUNCIÓN