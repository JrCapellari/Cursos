package poo.heranca.desafio;

public class Carro {
    // Atributos
    final int VELOCIDADE_MAXIMA;
    int velocidadeAtual;
    int delta = 5;

    //Construtor
    Carro(int velocidadeMaxima){
        VELOCIDADE_MAXIMA = velocidadeMaxima;
    }

    // Metodos
    void acelerar() {
        if(velocidadeAtual + delta > VELOCIDADE_MAXIMA){
            velocidadeAtual = VELOCIDADE_MAXIMA;
        }else {
            velocidadeAtual += delta;
        }
    }
    void frear() {
        if (velocidadeAtual >= delta) {
            velocidadeAtual -= delta;
        }else {
            velocidadeAtual = 0;
        }
    }
    public String toString() {
        return "Velocidade Atual: " + velocidadeAtual + "Km/h";
    }
}
