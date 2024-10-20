package fundamentos.operadores;

public class Logicos {
    public static void main(String[] args) {
        boolean con1 = true;
        boolean con2 = 3 > 7;

        System.out.println(con1 && con2); // e
        System.out.println(con1 || con2); // ou
        System.out.println(con1 ^ con2); // ou exc
        System.out.println(!con1); // negação
        System.out.println(!!con1); // dupla negação
        System.out.println(con1 && !con2); // negação + e

    }
}
