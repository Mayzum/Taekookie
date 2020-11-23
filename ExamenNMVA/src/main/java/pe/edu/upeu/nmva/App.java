package pe.edu.upeu.nmva;

import pe.edu.upeu.nmva.utils.LeerTeclado;
import pe.edu.upeu.nmva.utils.Menus_nmva;

public class App {

    public static void main(String[] args) {
        LeerTeclado teclado = new LeerTeclado();
        Menus_nmva menu = new Menus_nmva();

        menu.MenuOpcion(teclado);
    }

}
