#Medidas:

#AB = Diágonal mayor

#DC = Diágonal menor

#BD y BC = lados menores

#AD y AC = lados mayores

#El usuario ingresará las medidas  BC, CD y DA.

#Detalles de construcción

#Debemos tener en cuenta que la estructura del cometa estará dada 
#por un perímetro de varillas de plástico y los correspondientes
#entrecruces (DC y AB) del mismo material para mantener la forma 
#del cometa.

#El cometa estará construido con papel de alta resistencia. 
#La cola del mismo se construirá con el mismo papel que el cuerpo
#y representará un 10% adicional del necesario para el cuerpo.

#Necesitamos saber cuántos Mts de varillas de plástico y cuántos
#de papel son necesarios para la construcción en masa de 10 cometas.
#Tener en cuenta que los valores de entrada están expresados en Cms.

ladobc=int(input("ingrese los cmts bc"))

ladoda=int(input("ingrese los cmts da"))

ladocd=int(input("ingrese los cmts cd"))

perimetro1=ladocd*ladobc*2
perimetro2=ladocd*ladoda*2
perimetrototal=perimetro1 +perimetro2

papel_porce_extra=perimetrototal*0.1
papeltotal=perimetrototal+papel_porce_extra
varilla_por_10=perimetrototal*10
papel_por_10=papeltotal*10
varilla_en_metro=varilla_por_10/100
papel_en_metro=papel_por_10/100

print(f"la cantidad de metros de varillas {varilla_en_metro}\n y la cantidad de papel es {papel_en_metro} ")