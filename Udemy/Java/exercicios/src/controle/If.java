package controle;

import java.util.Scanner;

public class If {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Informe a media: ");
        double media = entrada.nextDouble();

        if (media >= 7.0) {
            System.out.println("Aluno Aprovado");
            System.out.println("Parabens!!!");

        }if (media >= 5.0 && media < 7.0) {
            System.out.println("Aluno Recuperacao");

        }if (media < 5.0){
            System.out.println("Aluno Reprovado");

        }

        entrada.close();

    }
}
