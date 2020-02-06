/*Debemos lograr tomar Los numeros por ID ,
transformarlos a enteros (parseInt),realizar la operación correcta y 
mostrar el resulto por medio de "ALERT"
ej.: "la Resta es 750"*/

function sumar() {
    var a;
    var b;
    var suma;
     a = document.getElementById("numeroUno").value;
     b = document.getElementById("numeroDos").value;
    a = parseInt(a);
    b = parseInt(b);
     suma = a + b;
    alert(suma);
}

function restar() {
    var a;
    var b;
    var resta;
     a = document.getElementById("numeroUno").value;
     b = document.getElementById("numeroDos").value;
    a = parseInt(a);
    b = parseInt(b);
    resta = a + b;
    alert(resta);
}

function multiplicar() {
    var a;
    var b;
    var multiplicador;
     a = document.getElementById("numeroUno").value;
     b = document.getElementById("numeroDos").value;
    a = parseInt(a);
    b =  parseInt(b);
    var multiplicador = a * b;
    alert(multiplicador);

}

function dividir() {
    var a;
    var b;
    var divisor;
     a = document.getElementById("numeroUno").value;
     b = document.getElementById("numeroDos").value;
    a = parseInt(a);
    b = parseInt(b);
     divisor = a % b;
    alert(divisor);
}