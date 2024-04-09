package poo.heranca.desafio;

public class Carro {
    // Atributos
    final int VELOCIDADE_MAXIMA;
    protected int velocidadeAtual;
    private int delta = 5;
    int ceta = 5;

    //Construtor
    protected Carro(int velocidadeMaxima){
        VELOCIDADE_MAXIMA = velocidadeMaxima;
    }

    // Metodos
   public void acelerar() {
        if(velocidadeAtual + getDelta() > VELOCIDADE_MAXIMA){
            velocidadeAtual = VELOCIDADE_MAXIMA;
        }else {
            velocidadeAtual += getDelta();
        }
    }
   public void frear() {
        if (velocidadeAtual >= ceta) {
            velocidadeAtual -= ceta;
        }else {
            velocidadeAtual = 0;
        }
    }
    public int getDelta() {
        return delta;
    }
    public void setDelta(int delta) {
        this.delta = delta;
    }
    public String toString() {
        return "Velocidade Atual: " + velocidadeAtual + "Km/h";
    }
}
