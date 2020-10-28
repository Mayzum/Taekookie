def PagoArticulosNMVA ():
    pago_por_todo = 0
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        precio = float (input ('Ingrese el valor de precio: '))
        descuento=precio*0.1
        if precio>=200:
            descuento=precio*0.15
        if precio>100 and precio<200:
            descuento=precio*0.12
        costo=precio-descuento
    pago_por_todo=pago_por_todo+costo
    print ('Valor de costo: ' + repr (costo))
    print ('Valor de descuento: ' + repr (descuento))
    print ()
    print ('Valor de pago por todo: ' + repr (pago_por_todo))
PagoArticulosNMVA()