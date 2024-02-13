package arrays;

import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Quantas notas gostaria de inserir: ");
        int tamArray = entrada.nextInt();

        double[] notas = new double[tamArray];
        for(int i = 0; i < notas.length; i++){
            System.out.print("Digite a nota " + (i+1) + ": ");
            notas[i] = entrada.nextDouble();
        }
        //System.out.println(Arrays.toString(notas));
        double total = 0;
        for (double nota : notas) {
            total += nota;
        }
        System.out.println("Média do aluno: " + (total/notas.length));
    }
}
