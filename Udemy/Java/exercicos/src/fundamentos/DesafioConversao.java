package fundamentos;

import java.util.Scanner;

public class DesafioConversao {
	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Digite o primeiro salario: ");
		String val01 = teclado.next().replace(",", ".");
		
		System.out.print("Digite o segundo salario: ");
		String val02 = teclado.next().replace(",", ".");
		
		System.out.print("Digite o terceiro salario: ");
		String val03 = teclado.next().replace(",", ".");
		
		double sal01 = Double.parseDouble(val01);
		double sal02 = Double.parseDouble(val02);
		double sal03 = Double.parseDouble(val03);
		
		double soma = (sal01 + sal02 + sal03);
		System.out.println("Soma = " + soma);
		System.out.println("Media = " + (soma/2));
		
		
		teclado.close();
	}

}
