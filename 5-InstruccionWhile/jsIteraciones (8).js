function mostrar()
{

	var contador=0;
	var positivo=0;
	var negativo=1;
	var numero;
	var respuesta='s';

	do{
		numero=parseInt(prompt("ingrese un numero"));
		while(isNaN(numero))
		{
			numero=prompt("no es un Numero. ingrese un numero");
		}

		if(numero<0)
		{	
			negativo=	negativo*numero ;
			contador++;




		}
		else
		{
			positivo=positivo+numero;




		}
		respuesta=prompt("quiere ingresar otro numero? ");
	}while(respuesta =='s')
	if (contador ==0)
	{
		negativo=contador

	}


document.getElementById('suma').value=positivo;
document.getElementById('producto').value=negativo;

}//FIN DE LA FUNCIÓN