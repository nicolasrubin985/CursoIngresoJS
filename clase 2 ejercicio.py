lamparas = int(input ("cuantas lamparas quieres comprar:"))
marcas = input("ingrese la marca: ") 
precio_de_lampara = 35
descuento=0
importefinal =0
importe_final_con_descuento=0
impuesto = 0
importe_con_iva= 0

if lamparas > 5: 
    importefinal = (lamparas *  precio_de_lampara )
    descuento = importefinal * 0.5
    importe_final_con_descuento = importefinal - descuento
           
elif   lamparas == 5 :
    if marcas == "Argentinaluz":
        importefinal= (lamparas* precio_de_lampara)
        descuento  = ((lamparas * precio_de_lampara ) *40)/100
        importe_final_con_descuento = importefinal - descuento
    else:
        importefinal =(lamparas * precio_de_lampara )
        descuento  = (lamparas * precio_de_lampara ) *0.3
        importe_final_con_descuento = importefinal - descuento
elif lamparas == 4 :
    if marcas ==    "Argentinaluz" or lamparas == "Felipelamparas":
        importefinal= (lamparas *precio_de_lampara)
        descuento  = (lamparas * precio_de_lampara ) *0.25
        importe_final_con_descuento = importefinal - descuento                   
    else:    
         importefinal= (lamparas *precio_de_lampara)
         descuento  = (lamparas * precio_de_lampara ) *0.20        
         importefinal_con_descuentos = importefinal - descuento
    
elif lamparas == 3:
    if marcas == "Argentinaluz":
        importefinal = (lamparas *precio_de_lampara )
        descuento = (lamparas* precio_de_lampara) *0.15
        importe_final_con_descuento = importefinal - descuento
    if marcas == "Felipelampara" :
        importefinal = (lamparas *precio_de_lampara )
        descuento  = (lamparas * precio_de_lampara ) *0.10 
        importefinal_con_descuento = importefinal - descuento
    else:
        importefinal = (lamparas *precio_de_lampara )
        descuento  = (lamparas * precio_de_lampara ) *0.05
        importefinal_con_descuento = importefinal - descuento  
if  importe_final_con_descuento > 120:
    impuesto  = importe_final_con_descuento * 0.10
    importe_con_iva= importe_final_con_descuento + impuesto

           
 
print("el precio final: ", importefinal)
print("el importe final con descuento es:", importe_final_con_descuento)
print("el importe con impuesto es: ",importe_con_iva)
print("cantidad de lamparas compradas: ",lamparas,"la marca es: ", marcas )


        
                    

