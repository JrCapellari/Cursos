package fundamentos;

import java.util.Scanner;

public class Wrappers {
	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		System.out.print("Digite um numero inteiro x3 : ");
		
		Byte b = 100; //byte
		Short s = 1000; //short
		Integer i = Integer.parseInt(teclado.next()); //int
		Long l = 100000L; //long
		Boolean bl = true; //boolean
		Boolean bo = Boolean.parseBoolean("false"); //String para boolean
		Character c = '#'; //char
		Float f = 123.10f; //float
		Double d = 321.10; //double
		
		System.out.println(b.byteValue() + " Byte");
		System.out.println(s.toString() + " Short para String"); //Será impresso como uma String
		System.out.println("Numero digitado: " + (i * 3));
		System.out.println(l + " Long");
		System.out.println(bl);
		System.out.println(bo.toString().toUpperCase()); // Será impresso como uma String
		System.out.println(c + "...");
		System.out.println(f);
		System.out.println(d);
		
		teclado.close();
	}

}
