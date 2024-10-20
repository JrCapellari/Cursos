package streams.desafiofiltro;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;

public class PodutoTeste {
    public static void main(String[] args) {
        Produto p1 = new Produto("NoteBook", 4564.80, 0.35, 0);
        Produto p2 = new Produto("Monitor", 589.90, 0.3, 0);
        Produto p3 = new Produto("Mouse", 89.90, 0.1, 0);
        Produto p4 = new Produto("Teclado", 120.00, 0.3, 0);
        Produto p5 = new Produto("impressora", 649.90, 0.3, 0);
        Produto p6 = new Produto("Heaset", 52.99, 0.1, 0);
        Produto p7 = new Produto("Microfone", 55.00, 0.1, 0);

        List<Produto> produtos = Arrays.asList(p1, p2, p3, p4, p5, p6, p7);

        // mostrar os produtos com 30% ou mais de desconto, frete gratis e relevantes
        //Filter - filter - map

        Predicate<Produto> superPromacao = p -> p.desconto >= 0.3;
        Predicate<Produto> freteGratis = p -> p.valorFrete == 0;
        Predicate<Produto> ProdRelevante = p -> p.preco >= 500;

        Function<Produto, String> chamadaPromocional = 
                p -> "Aproveite " + p.nome + " por R$" + p.preco;

        produtos.stream()
                .filter(superPromacao)
                .filter(freteGratis)
                .filter(ProdRelevante)
                .map(chamadaPromocional)
                .forEach(System.out::println);
    }

}
