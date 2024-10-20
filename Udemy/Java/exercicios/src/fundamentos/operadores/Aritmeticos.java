package fundamentos.operadores;

public class Aritmeticos {
	public static void main(String[] args) {
		
		// System.out.println(2 + 3);
		
		var x = 34.56; // Inferencia
		double y = 2.2;
		System.out.println(x + y);
		System.out.println(x - y);
		System.out.println(x * y);
		System.out.println(x / y);
		
		System.out.println("----------------------");
		
		int a = 8;
		int b = 3;
		System.out.println(a + b);
		System.out.println(a - b);
		System.out.println(a * b);
		System.out.println(a / b);
		System.out.println(a / (double)b); //Uso de cast
		
		System.out.println(a % b); //Resto da divisão (modulo)
		
		System.out.println(x + y - a * b);
		
	}

}
