package poo.composicao;

import java.util.ArrayList;

public class Compra {
    // Atributos
    String cliente;
    ArrayList<Item> itens = new ArrayList<>();

    // Metodos
    double obterValorTotal(){
        double total = 0;

        for (Item i : itens) {
            total += i.quantidade * i.preco;
        }

        return total;
    }
}
