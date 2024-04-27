package lambdas;

public class CalculoTeste2 {
    public static void main(String[] args) {
        Calculo calc = (x, y) -> {return x + y;};
        System.out.println(calc.executar(5, 7));

        calc = (x, y) -> x * y;
        System.out.println(calc.executar(2, 4));

        System.out.println(calc.legal());
        System.out.println(Calculo.muitolegal());

    }
}
