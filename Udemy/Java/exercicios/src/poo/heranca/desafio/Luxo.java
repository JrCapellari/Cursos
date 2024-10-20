package poo.heranca.desafio;

public interface Luxo {
    public void ligarAr();
    public void desligarAr();

    default int velocidadeAr() {
        return 1;
    }
}
