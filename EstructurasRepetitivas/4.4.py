def FabricaDeFocosNMVA():
    focos_verdes = 0
    focos_blancos = 0
    focos_rojos = 0
    n = int (input ('¿Cuantos focos desea?: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        print ('Seleccione el color que desea.')
        print ("1.- verde")
        print ("2.- blanco")
        print ("3.- rojo")
        color = 0
        while color<1 or color>3:
            color = int (input (': '))
        if color==1:
            focos_verdes=focos_verdes+1
        if color==2:
            focos_blancos=focos_blancos+1
        if color==3:
            focos_rojos=focos_rojos+1
        print ()
    print ('Cantidad de focos verdes: ' + repr (focos_verdes))
    print ('Cantidad de focos blancos: ' + repr (focos_blancos))
    print ('Cantidad de focos rojos: ' + repr (focos_rojos))
FabricaDeFocosNMVA()