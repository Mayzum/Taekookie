def OperacionArtcNMVA():
    #datos de entrada
    str
    operacion=int(input("(1) suma, (2) resta, (3) multiplicacion, (4) division, (5) potencia:"))
    dato1=int(input("ingresar el primer valor: "))
    dato2=int(input("ingresar el segundo valor: "))
    #proceso

    if (operacion==1) :
        suma=dato1+dato2
        print("el reultado es", suma)
    
    if (operacion==2) :
        resta=dato1-dato2
        print("el reultado es", resta)
    
    if (operacion==3) :
        multiplicacion=dato1*dato2
        print("el reultado es", multiplicacion)
    
    if (operacion==4) :
        division=dato1/dato2
        print("el reultado es", division)
    
    if (operacion==5) :
        potencia=dato1**dato2
        print("el reultado es", potencia)
OperacionArtcNMVA()