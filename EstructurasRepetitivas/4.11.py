import math as m
def FuncionExponencialNMVA ():
    exponente = 0
    factorial = 0
    x = float (input ('Ingrese el valor de x: '))
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        if i==1:
            exponente=1
            factorial=1
        factorial=factorial*i
        exponente=exponente+m.pow(x,i)/factorial
        print ()
    print ('Valor de ex: ' + repr (exponente))
    print ('Valor de factorial: ' + repr (factorial))
FuncionExponencialNMVA()