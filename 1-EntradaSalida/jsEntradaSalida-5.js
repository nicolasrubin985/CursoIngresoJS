/*Debemos lograr tomar nombre y edad por ID y mostrarlos concatenados 
ej.: "Usted se llama José y tiene 66 años" 	*/
function mostrar()
{	
    var a; 
    var b;
    a= document.getElementById("elNombre").value;   

    b = document.getElementById("laEdad").value; 
    alert("usted se llama " + a +  " y tiene " + b + " años" );
}

