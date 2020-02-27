function mostrar()
{
    var numero;
    var numerosPares;
     
    numero= parseInt(prompt("ingresar numero"));
    while(isNaN(numero))
    {
    numero=parseInt(prompt("dato invalido,ingresar un numero"));

    }
    for(var contador=0;contador<numero;contador++){

        if(numero%2==0)
        console.log("numeros div"+ contador);
        numerosPares++;
    }

    console.log("numeros pares :"+ numerosDiv);




}//FIN DE LA FUNCIÓN