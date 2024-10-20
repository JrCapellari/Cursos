package classes;

public class Produto {
// Atributos
    String nome;
    double preco;
    static double desconto = 0.25;

// Construtor
    // Construtor Padrão (sem parametros)
    Produto(){

    }
    // Construtor com parametros
    Produto(String nomeInicial){
        nome = nomeInicial;
    }

// Metodos
    double precoComDesconto(){
        return preco * (1 - desconto);
    }
    double descontoValor(){
        return preco * desconto;
    }
}
