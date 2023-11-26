package controle;

import java.util.Scanner;

public class DesafioDiaDaSemana {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um dia da semana: ");
        String dia = teclado.next();
        //System.out.println(dia);

        if (dia.equalsIgnoreCase("Domingo")) {
            System.out.println(dia + " - Primeiro dia da semana");

        }else if (dia.equalsIgnoreCase("Segunda-feira")) {
            System.out.println(dia + " - Segundo dia da semana");

        }else if (dia.equalsIgnoreCase("Terça-feira")){
            System.out.println(dia + " - Terceiro dia da semana");

        }else if (dia.equalsIgnoreCase("Quarta-feira")){
            System.out.println(dia + " - Quarto dia da semana");

        }else if (dia.equalsIgnoreCase("Quinta-feira")){
            System.out.println(dia + " - Quinto dia da semana");

        }else if (dia.equalsIgnoreCase("Sexta-feira")){
            System.out.println(dia + " - Sexto dia da semana");

        }else if (dia.equalsIgnoreCase("Sabado")){
            System.out.println(dia + " - Setimo dia da semana");

        }else {
            System.out.println(dia + " - Nao e um dia valido");

        }
        teclado.close();
    }

}
