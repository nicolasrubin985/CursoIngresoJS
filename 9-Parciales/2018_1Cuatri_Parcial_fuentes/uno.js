
function mostrar()
{
    var a;
    var b;
    var perimetro;

    var a=parseFloat(prompt("ingresar el largo:"));

    var b=parseFloat(prompt("ingrese el ancho:"));

    while(isNaN(a)||isNaN(b)){
        a=parseFloat(prompt("no es un numero,ingresar el largo:"));
        b=parseFloat(prompt("no es un numero,ingrese el ancho:"));

    }
        


}
