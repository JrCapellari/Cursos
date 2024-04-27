package lambdas;

@FunctionalInterface

public interface Calculo {
    // deve haver apenas um metodo abstrato
    double executar(double a, double b);

    // metodo default não interfere
    default String legal(){
        return "Legal";
    }
    // metodo static não interfere
    static String muitolegal(){
        return "Muito Legal";
    } 
}
