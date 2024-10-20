package lambdas;

import java.util.function.Predicate;

public class PredicadoComposicao {
    public static void main(String[] args) {
        Predicate<Integer> isPar = num -> num % 2 == 0;
        Predicate<Integer> isTresDigitos = 
        num -> num >= 100 && num <= 999;

        System.out.println(isPar.test(122));
        System.out.println(isTresDigitos.test(99));

        // Usando operadores logicos
        System.out.println(isPar.and(isTresDigitos).test(122));
        System.out.println(isPar.or(isTresDigitos).test(99));
        // Negando a linha anterior
        System.out.println(isPar.or(isTresDigitos).negate().test(99));
    }
}
