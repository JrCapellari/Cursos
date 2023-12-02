package arrays;
import java.util.Arrays;

public class exercicios {
    public static void main(String[] args) {
        
        double[] notasAlunoA = new double[3];

        notasAlunoA[0] = 7.9;
        notasAlunoA[1] = 8;
        notasAlunoA[2] = 6.7;

        System.out.println(Arrays.toString(notasAlunoA));
        System.out.println("Nota1 alunoA: " + notasAlunoA[0]);

        double totalAlunoA = 0;
        for(int i = 0; i < notasAlunoA.length; i++){
            totalAlunoA += notasAlunoA[i];
        }
        System.out.println("Media alunoA: " + totalAlunoA / notasAlunoA.length);
        
        System.out.println("----------------------------------------");
        // inicializando array por valores literais
        double[] notasAlunoB = {6.9, 8.7, 7.1, 10};

        System.out.println(Arrays.toString(notasAlunoB));
        System.out.println("Nota2 alunoB: " + notasAlunoB[1]);

        double totalAlunoB = 0;
        for(int i = 0; i < notasAlunoB.length; i++){
            totalAlunoB += notasAlunoB[i];
        }
        System.out.println("Media alunoB: " + totalAlunoB / notasAlunoB.length);
    }
}