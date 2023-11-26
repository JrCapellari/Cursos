package classe;

public class ProdutoTeste {
    public static void main(String[] args) {
        Produto p1 = new Produto("Notebook"); // Usando construtor explicito
        // p1.nome = "Notebook";
        p1.preco = 4350.00;
       // p1.desconto = 0.25;

        var p2 = new Produto(); // Usando construtor padão
        p2.nome = "Caneta Preta";
        p2.preco = 12.56;
       // p2.desconto = 0.29;

        // Produto.desconto = 0.30;
        System.out.println(Produto.desconto);
        System.out.printf("Produto: %s\nPreco: %.2f\nDesconto: %.2f", p1.nome, p1.preco, p1.descontoValor());
        System.out.printf("\nPreco com Desconto: R$ %.2f\n", p1.precoComDesconto());
        System.out.println("-------------------------------");
        System.out.printf("Produto: %s\nPreco: %.2f\nDesconto: %.2f", p2.nome, p2.preco, p2.descontoValor());
        System.out.printf("\nPreco com Desconto: R$ %.2f ", p2.precoComDesconto());
    }
}
