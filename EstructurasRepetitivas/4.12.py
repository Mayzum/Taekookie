def cajaRegistradoraNMVA():
    t=0
    billetes1000=int(input("Ingrese el valor de billetes de 1000 :"))
    billetes500=int(input("Ingrese el valor de billetes de 500 :"))
    billetes100=int(input("Ingrese el valor de billetes de 100 :"))
    billetes200=int(input("Ingrese el valor de billetes de 200 :"))
    billetes50=int(input("Ingrese el valor de billetes de 50 :"))
    billetes20=int(input("Ingrese el valor de billetes de 20 :"))
    monedas1=int(input("Ingrese el valor de monedas 1 :"))
    monedas2=int(input("Ingrese el valor de monedas de 2 :"))
    monedas5=int(input("Ingrese el valor de monedas de 5 :"))
    t=(billetes1000*1000)+(billetes500*500)+(billetes100*100)+(billetes200*200)+(billetes50*50)+(billetes20*20)+(monedas2*2)+(monedas5*5)+monedas1
    print("\nLa caja registradora almaceno un total de:",t,"\n")
cajaRegistradoraNMVA()