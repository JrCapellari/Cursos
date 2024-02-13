package arrays;

import java.util.Arrays;
import java.util.Scanner;

public class Matriz {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Quantos alunos? ");
        int quantAlunos = entrada.nextInt();
        System.out.print("Quantas notas por aluno? ");
        int quantNotas = entrada.nextInt();

        double[][] notasTurma = new double[quantAlunos][quantNotas];

        double total = 0;
        for(int a = 0; a < notasTurma.length; a++ ){
            for(int n = 0; n < notasTurma.length; n++){
                System.out.printf("Informe a nota %d do Aluno %d: ", 
                (n+1), (a+1));
                notasTurma[a][n] = entrada.nextDouble();
                total = notasTurma[a][n];
            }
        }
        double media = total / (quantAlunos * quantNotas);
        System.out.print("Média da turma é: " + media);
        for (double[] notasAluno : notasTurma) {
            System.out.print(Arrays.toString(notasAluno));
        }
    }
}
