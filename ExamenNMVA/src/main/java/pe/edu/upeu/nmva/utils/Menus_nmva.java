package pe.edu.upeu.nmva.utils;

import pe.edu.upeu.nmva.Examen.ResolucionExamen;

public class Menus_nmva {

    public static void MenuOpcion(LeerTeclado teclado) {
        System.out.println( "*********************Bienvenidos al Sistema********************" );
        int numberOption;
        ResolucionExamen examen = new ResolucionExamen();

        System.out.println(
                "Seleccione la opcion que desee :\n(1)Ejercicio1 Automoviles \n(2)Ejercicio2 Tabla de multiplicar\n(3)Ejercicio3 NumerosPerfectos \n(4)Ejercicio4 ValorX \n(0)Salir\n");
        System.out.print("\n= ");
        numberOption = teclado.leer(3);

        switch (numberOption) {
            case 1:
                examen.ejercicio1_autos();
                repeatCicle(teclado);
                break;
            case 2:
                examen.ejercicio2_tabla();
                repeatCicle(teclado);
                break;
            case 3:
                examen.ejercicio3_numeroperfec();
                repeatCicle(teclado);
                break;
            case 4:
                int n, e;
                System.out.println("Ingrese el numero base: ");
                n = teclado.leer(0);
                System.out.println("Ingrese el numero exponente: ");
                e = teclado.leer(0);

                System.out.println(examen.ejercicio4_valorX(n, e));
                repeatCicle(teclado);
                break;
            case 0:
                System.out.println("Eso es todo gracias");
                break;
            default:
                System.out.println("ERROR no existe ese valor");
                repeatCicle(teclado);

        }
    }

    public static void repeatCicle(LeerTeclado teclado) {
        int numberOption;
        System.out.print("\n\nDeseas volver al Menu: \n(1) SI \n(2) NO \n\n= ");
        numberOption = teclado.leer(3);

        if (numberOption == 1) {
            MenuOpcion(null);
        } else if (numberOption == 2) {
            System.out.println("\nEso es todo gracias");
        } else {
            System.out.println("\nERROR no existen esas opciones");
            repeatCicle(null);
        }
    }
}
