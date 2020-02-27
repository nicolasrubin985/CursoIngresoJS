function mostrar()
{
    var letra;
    var numero;
    var contPares=0;
    var contInpares=0;
    var cantCeros;
    var contPos=0;
    var contNega=0;
    var promPost;
    var promNeg;
    var flag=0;
    var max;
    var min;
    var letraMayor;
    var letraMenor;
    var contador;
    var sumaNeg;
    

    var seguir;




    do{
        letra= prompt("ingrese una letra: ");
        while(!((letra>= 'A'&& letra<='Z')||(letra>='a'&& letra <='z'))){
            letra= prompt("dato invalido. ingrese una letra: ");

        }
        numero = parseInt(prompt("ingrese un numero -100 y 100"));
        while(numero < -100 || numero>100 || isNaN(numero)){
            numero = parseInt(prompt("dato invalido. ingrese un numero -100 y 100"));
        }
        //me fijo la paridad
        if(numero%2==0){
            contPares++;
        }
        else{
            contInpares++;
        }
        //me fijo el signo
        if(numero>0){
            contPos++;
            contador++;

        }
        else if (numero<0){
            contNega++;
            sumaNeg=contNega+numero;
        }    
        else{
            cantCeros++;
        }
        //busco max y min
        if(numero>max || flag==0){
            max=numero;
            letraMayor=letra;
        }
        if(numero<min||flag==0){
            min=numero;
            letraMenor=letra;
            flag=1;
        }
        
      seguir=prompt("quiere continuar?: ");
    }while(seguir =='s')

    promPost=contPos/contador;

    document.write("cantidad de numPares: "+contPares
                +"</br>cantidad de numImpares: "+contInpares+
                +"</br> cantidad de Ceros: "+cantCeros
                +"</br> prom de los numPos: "+promPost
                +"</br> suma de todos los Negativos: "+sumaNeg
                +"</br> numero max"+max
                +"</br> letra max" +letraMayor
                +"</br> letra menos"+ letraMenor
                +"</br> num min"+min);
    



}
