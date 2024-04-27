package lambdas;

import java.util.function.Function;

public class Funcao {
    public static void main(String[] args) {
        Function<Integer, String> parOuImpar = 
        numero -> numero % 2 == 0 ? "Par" : "Impar";

        Function<String, String> resultado = 
        valor -> "O resultado é " + valor;

        Function<String, String> empolgado = 
        valor -> valor + "!!!";

        Function<String, String> duvida =
        valor -> valor + "???";

        String resultadoFinal1 = 
        parOuImpar.andThen(resultado).andThen(empolgado).apply(32);

        String resultadoFinal2 =
        parOuImpar.andThen(resultado).andThen(duvida).apply(33);

        System.out.println(resultadoFinal1);
        System.out.println(resultadoFinal2);
        System.out.println(parOuImpar.apply(32));
    }
}
