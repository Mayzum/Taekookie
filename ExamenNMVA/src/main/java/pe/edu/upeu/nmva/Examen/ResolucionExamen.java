package pe.edu.upeu.nmva.Examen;

import pe.edu.upeu.nmva.utils.LeerTeclado;

public class ResolucionExamen {

    public static LeerTeclado teclado = new LeerTeclado();

     public void ejercicio1_autos() {
         int cant_auto=0,costo=0,categoria=0,categoria1=0,categoria2=0,categoria3=0;
         double impuesto=0, impuesto_total=0;

         System.out.println("¿Cuantos automoviles tienes?");
         cant_auto= teclado.leer(0);
         for (int i = 1; i <= cant_auto; i++) {
             System.out.println("¿Que categoria es tu automovil?");
             categoria=teclado.leer(0);
             System.out.println("¿Cuanto es el costo del automovil?");
             costo=teclado.leer(0);
             if (categoria==1) {
                 impuesto=costo*0.1;
                 categoria1=(int)(categoria1+impuesto);
                }
                 if (categoria==2) {
                 impuesto=costo*0.07;
                 categoria2=(int)(categoria1+impuesto);
                }
                 if (categoria==3) {
                 impuesto=costo*0.05;
                 categoria3=(int)(categoria1+impuesto);

                }
                impuesto_total=impuesto_total+impuesto;
                System.out.println("El valor del impuesto es:"+impuesto);
                System.out.println("");     
                
            }

            System.out.println("La categoria 1 apagar es"+categoria1);
            System.out.println("La categoria 2 apagar es"+categoria2);
            System.out.println("La categoria 3 apagar es"+categoria3);
            System.out.println("El total a pagar es"+impuesto_total);   
        }

    public void ejercicio2_tabla() {
        int numllegada, numpartida, multiplicado;
        System.out.println("Digite su numero partida");
        numpartida=teclado.leer(0);
        System.out.println("Digite el valor de llegada");
        numllegada=teclado.leer(0);
        for (int i = numpartida; i < numllegada; i++) {
            for (int j = 0; j <= 12; j++) {
                multiplicado = i * j;
                System.out.println(i + "x"+j+"="+ multiplicado);

            }
        }
    }


    public void ejercicio3_numeroperfec() {
        int i=1, s=0,num;
        System.out.println("Escribe un numero");
        num=teclado.leer(0);

        while (i<num){ 
            if(num%i==0) { 
               s = s + i;
            }
            i++;
    }  

    if (s==num) { 
        System.out.println("Perfecto");

    } else { 
        System.out.println("No es perfecto");

    }

}  


    public int ejercicio4_valorX(int n, int e) {
        if (e <= 0) {
            return 1;
        } else {
            return n * ejercicio4_valorX(n, e - 1);
        }
    }

}
