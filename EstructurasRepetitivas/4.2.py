import sys
def ElNaufragoHamburguesasNMVA():
    pago = 0
    n = int(input('¿Cuantas hamburguesas desea?: '))
    for i in range(1, n + 1):
        print('PROCESO ' + repr(i))
        print('Seleccione el tipo de hamburguesa.')
        print('\t1.- S sencilla')
        print('\t2.- D doble')
        print('\t3.- T triples')
        sys.stdout.write('\t')
        tipo_de_hamburguesa = 0
        while tipo_de_hamburguesa < 1 or tipo_de_hamburguesa > 3:
            tipo_de_hamburguesa = int(input(': '))
            if tipo_de_hamburguesa < 1 or tipo_de_hamburguesa > 3:
                sys.stdout.write(
                    'Valor incorrecto. Ingr\u00E9selo nuevamente.')
        costo = 0
        if tipo_de_hamburguesa == 1:
            costo = 20
        if tipo_de_hamburguesa == 2:
            costo = 25
        if tipo_de_hamburguesa == 3:
            costo = 28
        print('Seleccione la forma de pago.')
        print('\t1.- Efectivo')
        print('\t2.- Tarjeta')
        sys.stdout.write('\t')
        forma_de_pago = 0
        while forma_de_pago < 1 or forma_de_pago > 2:
            forma_de_pago = int(input(': '))
            if forma_de_pago < 1 or forma_de_pago > 2:
                sys.stdout.write(
                    'Valor incorrecto. Ingr\u00E9selo nuevamente.')
        if forma_de_pago == 1:
            cargo = 0
        else:
            cargo = costo*0.05
        pago = pago+costo+cargo
        print('Valor de cargo es: ' + repr(cargo))
        print('Valor de costo es: ' + repr(costo))
        print()
    print('Valor de pago es: ' + repr(pago))
ElNaufragoHamburguesasNMVA()