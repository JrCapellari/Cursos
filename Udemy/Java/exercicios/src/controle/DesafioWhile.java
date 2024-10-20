package controle;

import java.util.Scanner;

public class DesafioWhile {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);
        int op = 0;
        double nota = 0;
        double total = 0;
        String SN = "n";

        while (nota != -1){
            System.out.print("Digite a nota (ou -1 para sair): ");
            nota = teclado.nextDouble();

            if (nota >= 0 && nota <= 10){
                total += nota;
                op++;
            }else if (nota != -1){
                System.out.println("Insira uma nota entre 0 e 10");
            }
        }
        double media = total/op;
        System.out.println("Media do aluno: " + media);
        System.out.println(total);
        System.out.println(op);

    }
}
