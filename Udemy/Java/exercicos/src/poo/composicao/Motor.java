package poo.composicao;

public class Motor {

    // Atributos
    boolean ligado = false;
    double fatorInjecao = 1;

    // Metodos
    int giros(){
        if (!ligado) {
            return 0;
        } else {
            return (int) Math.round(fatorInjecao * 3000);
        }
    }
}
