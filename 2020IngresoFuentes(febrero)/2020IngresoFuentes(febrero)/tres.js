function mostrar()
{
	var nombre;
	var edad;
	var sexo;
	var Ecivil;
	var contador;
	var seguir;

	nombre=prompt("ingresar su nombre");

	do
	{
		do
		{
			edad=prompt("ingresar el edad mayor a 18");
			edad=parseInt(edad);

	}while(isNaN(edad)||edad>=18);
	
	
		
	

	seguir=prompt("desea seguir? ");
	}while(seguir='s')
}
