package lambdas;

public class CalculoTeste1 {
    public static void main(String[] args) {
        Calculo calculo = new Somar();
        System.out.println(calculo.executar(7, 5));

        calculo = new Multiplicar();
        System.out.println(calculo.executar(4, 2));

    }
}
