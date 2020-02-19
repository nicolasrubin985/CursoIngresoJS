function mostrar()
{
	var a;
	var b;
	var contador=0;
	var acumulador=0;
	
	
		do
		{	
			a=parseInt(prompt("ingresar un numero "));
			acumulador=a+acumulador;
			con++;
			b=prompt("queres continuar");

			
			









		}while(b =='si');

	

	
		document.getElementById('suma').value=acumulador;
		document.getElementById('promedio').value=acumulador/contador;

		
		

	}


//do while se utiliza cuando se tiene que ejecutar una sola vez
//for cuando sabes cuantas veces tenes que hacer la suma


}//FIN DE LA FUNCIÓN