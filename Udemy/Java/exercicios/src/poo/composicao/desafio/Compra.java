package poo.composicao.desafio;

import java.util.ArrayList;
import java.util.List;

public class Compra {
    // Atributos
    final List<Item> itens = new ArrayList<>();

    // Metodos
    void adiconarItem(Produto p, int qtde){
        this.itens.add(new Item(p, qtde));
    }

    void adiconarItem(String nome, double preco, int qtde){
        var produto = new Produto(nome, preco);
        this.itens.add(new Item(produto, qtde));
    }

    double obterValorTotal(){
        double total = 0;

        for (Item item : itens) {
            total += item.quantidade * item.produto.preco;
        }

        return total;

    }

}
