package fundamentos.operadores;

public class DesafioLogico {
    public static void main(String[] args) {
        boolean trab1 = false;
        boolean trab2 = true;

        boolean tv50 = (trab1 && trab2); // and (e)
        boolean tv32 = (trab1 ^ trab2); // xor (ou exclusivo)
        boolean sorv = (trab1 || trab2); // or (ou)
        System.out.println("Compramos TV 50 e tomamos sorvete - " + tv50);
        System.out.println("Compramos TV 32 e tomamos sorvete - " + tv32);
        System.out.println("Sem TV e sem sorvete - " + !sorv);
    }
}
