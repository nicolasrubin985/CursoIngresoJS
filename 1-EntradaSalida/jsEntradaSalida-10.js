/*Debemos lograr tomar el importe por ID.
Transformarlo a entero (parseInt), luego
mostrar el importe con un Descuento del 25 %
en el cuadro de texto "RESULTADO"*/
function mostrarAumento()
{
    var a ;
    var resultado;

    a=document.getElementById("importe").value;


    a=parseInt(a);
    resultado=a-((a*25)/100);
    document.getElementById("resultado").value = resultado;


}
