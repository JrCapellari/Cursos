package fundamentos.operadores;

public class Ternarios {
    public static void main(String[] args) {

        double media = 7.6;
        String result = media >=7.0 ? "Aprovado" : "Recuperação"; // Op. Ternario
        System.out.println(result);

        double nota = 7.3;
        boolean bomComp = true;
        boolean passMedia = nota >= 7;
        boolean temDesc = bomComp && passMedia;
        String resultado = temDesc ? "sim" : "nao";
        System.out.println("Tem desconto? " + resultado);
    }
}
