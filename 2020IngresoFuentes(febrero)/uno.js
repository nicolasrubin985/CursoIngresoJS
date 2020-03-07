
function mostrar()
{
	var productos;
  
  var precio;
  var cantidad;
  var marca;
  var fabricante;

   
    for(i=0;i<5;i++)
    {
		do
		{
			productos=prompt("ingrese el tipo de producto: jabon , barbijo, alcohol");

		}while(!isNaN(productos)||productos!="barbijo"&&productos!="jabon"&&productos!="alcohol");

		do
		{
			precio=prompt("ingresar el precio entre 100 y 300");
			precio=parseInt(precio);

		}while(isNaN(precio)||precio<100&&precio<300);

		do
		{
			cantidad=prompt("ingresar el cantidad entre 1 y 1000");

		}while(isNaN(cantidad)||cantidad<1&&cantidad>1000);
		

	}
	alert(productos);

	/*if (contador ==0|| mayorcantidadunidades<cantidad)
		mayorcantidadunidades=cantidad
		mayorcantidadunidades=fabricante
	*/
	/*if(tipo=="barbijo"&&barbijomascaro<precio ||banderabarbijo==0
		barbijomascaro=barbijo
			"			cantidad=cantidad
			"			fabricante=fabricante
			banderabarbijo=1
}	
