package poo.composicao.desafio;

public class Sistema {
    public static void main(String[] args) {
        
        Compra compra1 = new Compra();
        compra1.adiconarItem("Caneta, 9.67", 1, 100);
        compra1.adiconarItem("Notebook", 2000, 2);

        Compra compra2 = new Compra();
        compra2.adiconarItem("Caderno", 10, 10);
        compra2.adiconarItem("Impressora", 1000, 1);

        Cliente cliente = new Cliente("Maria Julia");
        cliente.adicionarCompra(compra1);
        cliente.adicionarCompra(compra2);

        System.out.println(cliente.obterValorTotal());
    }

}
