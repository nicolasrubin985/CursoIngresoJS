function mostrar()
{
    var edad;
    var sexo;
    var promedioNtotales;
    var notas;
    var acumnotas=0;
    var notaBaja=0;
    var SexoBajo=0;
    var flag=0;
    var contVarones6=0;

    for(var i=1;i<=5;i++){
    edad=parseInt(prompt("ingresar la edad"));
    
    notas=parseInt(prompt("ingresar las notas(0-10"));
    while(notas>=0 ||nota<=10||isNaN(nota)){
        notas=parseInt(prompt("dato invalido,ingresar las notas"));
    }
    sexo=parseInt(prompt("ingresar sexo").toLocaleLowerCase);
    while(sexo != 'm'&& sexo != 'f'){
        sexo=parseInt(prompt("sexo invalido, ingresar sexo").toLocaleLowerCase);
    }
    acumnotas=acumnotas+nota;
    if(nota<notaBaja|| flag==0){

        notaBaja=nota;
        flag=1;
        SexoBajo=sexo;
    }
    if(sexo=='m' && nota>=6){
        contVarones6++;
    }
}
promedioNtotales=acumnotas/5;
alert("promedio notas"+ promedioNtotales +"\n nota mas baja "+ notaBaja+"\n sexo de la persona de nota baja"+SexoBajo+ "\n cantidad de varones mas de 6"+contVarones6);

    
   


    
    
}
