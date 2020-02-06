/*Debemos lograr tomar Los numeros por ID ,
transformarlos a enteros (parseInt),realizar la operación correcta y 
mostrar el resto entre el dividendo y el divisor.
ej.: "El resto es 0 ."*/
function SacarResto()
{
    var a;  
    var b;
    var resto;
     a = document.getElementById("numeroDividendo").value;
     b = document.getElementById("numeroDivisor").value;
    a =parseInt(a);
    b =parseInt(b);
    resto= a % b;
    // modulo % te da el resto de una division entera
    
    
    alert("El resto es "+resto);
}
