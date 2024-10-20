package colecoes;

import java.util.ArrayList;
import java.util.List;

public class Lista {
    public static void main(String[] args) {
        List<Usuario> lista = new ArrayList<>();
        
        Usuario u1 = new Usuario("Ana");
        lista.add(u1);

        lista.add(new Usuario("Carlos"));
        lista.add(new Usuario("Lia"));
        lista.add(new Usuario("Bia"));
        lista.add(new Usuario("Manu"));

        //System.out.println(lista);
        //System.out.println(lista.size());

        int ind = 1;
        System.out.println("indice " + ind + " usuario " + lista.get(ind).nome);

        for (Usuario u : lista) {
            System.out.println(u.nome);
        }
    }
}
