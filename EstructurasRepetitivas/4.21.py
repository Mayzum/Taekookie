def cajaRegistradoraNMVA():
    total=0
    billetes50=int(input("Ingrese el valor de billetes de 50 :"))
    billetes10=int(input("Ingrese el valor de billetes de 10 :"))
    billetes20=int(input("Ingrese el valor de billetes de 20 :"))
    monedas5=int(input("Ingrese el valor de monedas 5 :"))
    monedas10=int(input("Ingrese el valor de monedas de 10 :"))
    moneda1=int(input("Ingrese el valor de monedas un peso:"))
    total=(billetes10*10)+(billetes20*20)+(billetes50*50)+(monedas5*5)+(moneda1*1)+(monedas10*10)
    print("La caja registradora almaceno un total de:",total)
cajaRegistradoraNMVA()