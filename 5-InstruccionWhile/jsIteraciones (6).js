function mostrar()
{
	var numero1;
	var con=0;
	var acu=0;
	var prom;
	
	
	while(con<5 )
	{

		numero1 = parseInt(prompt("siguiente numero "));
		while(isNaN(numero1))
		{
			numero1=parseInt(prompt("no es numero escribir numero "));
		}
		
		acu= numero1+acu;
		con++


	}
	 prom=acu/5;
	


document.getElementById('suma').value=acu;
document.getElementById('promedio').value=prom;

}//FIN DE LA FUNCIÓN