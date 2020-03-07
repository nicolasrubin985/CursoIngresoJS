function mostrar()
{
  var tipo;
  var peso;
  var precioporkg;
  
 
  do
  {

    do
		{
			tipo=prompt("ingrese el tipo de los ingredientes  ");

		}while(!isNaN(tipo)||tipo=='v'&&tipo=='a'&&tipo=='m');

    do
		{
			precio=prompt("ingresar el precio entre 100 y 300");
			precio=parseInt(precio);

    }while(isNaN(precio)||precio>0);
   
    do
		{
			precio=prompt("ingresar el precio entre 100 y 300");
			precio=parseInt(precio);

    }while(isNaN(precio)||precio>=10&&precio<=1000);
    

    

  }


    
  

}
