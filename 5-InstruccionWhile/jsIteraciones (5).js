function mostrar()
{

var sexo = prompt("ingrese f ó m .").toLocaleLowerCase();// tolocalelowercase pasar letras a minusculas
//toupcase pasar a mayuscula
// una sola comilla un solo caracter, ""variables de caracteres
while (!(sexo =='f' || sexo =='m'  ))
{

    sexo =prompt("ingrese si es masculino o fem").toLocaleLowerCase;




}



document.getElementById('Sexo').value=sexo;

}//FIN DE LA FUNCIÓN