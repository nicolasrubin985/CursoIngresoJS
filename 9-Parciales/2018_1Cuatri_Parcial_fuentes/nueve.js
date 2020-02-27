function mostrar()
{
    var marca; 
    var peso;
   var temperatura; 
   var cantidadTpares=0;
    var marcaPmasPesado;
     var Conservan0=0;
     var promPeso;
      var pesomax;
       var pesomin;
       var flag=0;
       var seguir;
       
       do{


        marca=prompt("ingresar la marca");

        peso=parseFloat(prompt("ingresar el peso"));

        while(peso>100|| peso<1||isNaN(peso)){
            peso=parseFloat(prompt("dato invalido. ingresar el peso"));
        }
        temperatura= parseFloat(prompt("ingresar temperatura"));

        while(temperatura<-30|| tempratura> 30 || isNaN(temperatura)){
            temperatura= parseFloat(prompt("dato invalido. ingresar temperatura"));
        }
        if(temperatura%2==0){
            cantidadTpares++;
        }
        if(peso>pesomax|| flag==0){
            pesomax=peso;
            marcaPmasPesado=marca;
            ;
        }
        if(peso<pesomin|| flag==0){
            pesomin=peso;
            
        }
        if(temperatura<0){
            Conservan0++;
        }
        contador++
        







        seguir=prompt("quiere continuar?: ");

       }while(seguir=='s')
       promPeso=acum


}   document.write("cantidad de numPares: "+contPares
+"</br>cantidad de numImpares: "+contInpares+
+"</br> cantidad de Ceros: "+cantCeros
+"</br> prom de los numPos: "+promPost
+"</br> suma de todos los Negativos: "+sumaNeg
+"</br> numero max"+max
+"</br> letra max" +letraMayor
+"</br> letra menos"+ letraMenor
+"</br> num min"+min);

