package classe;

public class AreaCirc {
// Atributos
    double raio;
    static final double PI = 3.1415; // variavel da classe - constante

// Construtor
    AreaCirc(double raioInicial){
        raio = raioInicial;
    }

// Metodos
    double area(){
        return PI * Math.pow(raio, 2);
    }
    static double area(double raio){
        return  PI * Math.pow(raio, 2);
    }
}
