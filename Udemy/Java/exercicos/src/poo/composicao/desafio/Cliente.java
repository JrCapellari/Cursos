package poo.composicao.desafio;

import java.util.ArrayList;
import java.util.List;

public class Cliente {
    // Atributos
    final String nome;
    final List<Compra> compras = new ArrayList<>();

    // Metodos
    Cliente(String nome){
        this.nome = nome;
    }

    void adicionarCompra(Compra compra){
        this.compras.add(compra);
    }

   double obterValorTotal(){
        double total = 0;

    for (Compra compra : compras) {
        total += compra.obterValorTotal();
    }

    return total;

   }
}
