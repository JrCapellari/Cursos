package poo.composicao.desafio;

public class Item {
    // Atributos
    final int quantidade;
    final Produto produto;

    // Metodos
    Item(Produto produto, int quantidade){
        this.produto = produto;
        this.quantidade = quantidade;
    }
}
