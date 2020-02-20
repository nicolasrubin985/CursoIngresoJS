function mostrar()
{
	// declarar variables
	var numero;
	var maximo;
	var minimo;
	var respuesta;
	var flag=0;

	
	
	do{	
		//pido un numero

		numero=prompt("ingrese un numero");
		
		//verifico que sea un numero
		
		while(isNaN(numero))
		{

			numero=prompt("no es un numero. ingrese un numero");

		}
		if(flag ==0||numero>maximo)
		{
			maximo=numero;
		}
		if(flag == 0 || numero<minimo)
		{
			minimo=numero;
			flag=1
		}

		respuesta=prompt("quiere ingresar otro numero");
	}while (respuesta=='s');


	document.getElementById("maximo").value=maximo;
	document.getElementById("minimo").value=minimo;




	



}//FIN DE LA FUNCIÓN1