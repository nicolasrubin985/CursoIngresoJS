function mostrar()
{

    var numero;
    var numerosDiv=0;
     
    numero= parseInt(prompt("ingresar numero"));
    while(isNaN(numero))
    {
    numero=parseInt(prompt("dato invalido,ingresar un numero"));

    }
    for(var contador=1;contador<=numero;contador++){

        
        if(numero%contador==0)
        console.log("numeros div"+ contador);
        numerosDiv++;


    }
    console.log("cantidad de divencontrados:"+numerosDiv);


}//FIN DE LA FUNCIÓN