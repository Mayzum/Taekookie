package pe.edu.upeu.nmva.utils;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LeerTeclado {
    public static BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));

    public static String leer(String dato) {
        try {
            dato = teclado.readLine();
        } catch (Exception e) {
            System.err.println("ERROR string" + e.getMessage());
        }
        return dato;
    }

    public static int leer(int dato) {
        try {
            dato = Integer.parseInt(teclado.readLine());
        } catch (Exception e) {
            System.err.println("ERROR int" + e.getMessage());
        }
        return dato;
    }
    
    public static double leer(double dato) {
        try {
            dato = Double.parseDouble(teclado.readLine());
        } catch (Exception e) {
            System.err.println("ERROR double" + e.getMessage());
        }
        return dato;
    }
    
    public static float leer(float dato) {
        try {
            dato = Float.parseFloat(teclado.readLine());
        } catch (Exception e) {
            System.err.println("ERROR float" + e.getMessage());
        }
        return dato;
    }
    
    public static boolean leer(boolean dato) {
        try {
            dato = Boolean.parseBoolean(teclado.readLine());
        } catch (Exception e) {
            System.err.println("ERROR boolean" + e.getMessage());
        }
        return dato;
    }
}
