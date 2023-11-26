package fundamentos;

import java.util.Scanner;

public class Console {
	public static void main(String[] args) {
		System.out.print("Ola");
		System.out.print(" Mundo!");
		
		System.out.println(" desejo um");
		System.out.print("Bom");
		System.out.println(" dia!\n");
		System.out.print("Para".toUpperCase());
		System.out.print(" Todos\n \n" .toUpperCase());
		
		System.out.printf("Sorteio: %d %d %d %d %d %d\n", 1, 2, 3, 4, 5, 6);
		System.out.printf("Premio R$ %.2f\n", 1345.7852369);
		System.out.printf("Nome: %s\n\n", "Pedro");
		
		Scanner teclado = new Scanner(System.in);
		System.out.print("Digite seu nome ");
		String nome = teclado.nextLine();
		System.out.print("Digite seu sobrenome: ");
		String sobrenome = teclado.nextLine();
		System.out.print("Digite sua idade: ");
		int idade = teclado.nextInt();

		
		System.out.printf("%s %s tem %d anos", nome, sobrenome, idade);
		//System.out.println("Seu nome e: " + nome + " Idade: " + idade);
		
		teclado.close();
	}
}
