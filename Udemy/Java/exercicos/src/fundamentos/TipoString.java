package fundamentos;

public class TipoString {
	public static void main(String[] args) {
		System.out.println("Ola pessoal".charAt(2));
		
		String s = "Boa tarde";
		System.out.println(s.concat("!!!")); // (s. + "!!!")
		System.out.println(s.startsWith("Boa"));
		System.out.println(s.toLowerCase().startsWith("boa"));
		System.out.println(s.toUpperCase().endsWith("TARDE"));
		System.out.println(s.length());
		System.out.println(s.toLowerCase().equals("boa tarde"));
		System.out.println(s.equalsIgnoreCase("boa tarde"));
		
		var nome = "Pedro"; // String por inferencia
		var sobrenome = "Santos";
		var idade = 33;
		var salario = 1234.98;
		
		System.out.printf("O senhor %s %s tem %d anos e ganha R$%.2f ", nome, sobrenome, idade, salario);
		
		String frase = String.format("\nO senhor %s %s tem %d anos e ganha R$%.2f ", 
				                      nome, sobrenome, idade, salario);
		System.out.println(frase);
		
	}

}
