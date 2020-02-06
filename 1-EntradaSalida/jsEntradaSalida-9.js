/*Debemos lograr tomar el importe por ID ,
transformarlo a entero (parseInt), luego
mostrar el importe con un aumento del 10 %
en el cuadro de texto "RESULTADO".*/
function mostrarAumento()
{
var a;
//paso1

var incremento;
 a= document.getElementById("sueldo").value;

 
a= parseFloat(a);
//paso 2 
incremento = a+((a*10)/100);

//paso 3

document.getElementById("resultado").value = incremento;
	
}
