def VacunacovidNMVA():
 str
 tipoA=int(0)
 tipoB=int(0)
 tipoC=int(0)
 for x in range(0,1):
    edad=int(input("ingresar la edad:"))
    sexo=int(input("ingresar el sexo >>[1:varon;2:mujer]:"))
    if (edad>70) :
           print("se aplicara la vacuna tipo C")
           tipoC=tipoC+1
    if (edad>15 and edad <70 and sexo==2):
        print("se aplicara vacuna B")
        tipoB=tipoB+1
    if(sexo==1 or (edad<16)):
        print("se aplicara vacuna tipo A")
        tipoA=tipoA+1
VacunacovidNMVA()