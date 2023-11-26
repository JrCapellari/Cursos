package fundamentos;

public class Inferencia {
	public static void main(String[] args) {
		
		double a = 4.5;
		System.out.println(a);
		
		var b = 4.5; //detecta por inferencia
		System.out.println(b);
		
		var c = "texto por inferencia"; //detecta por inferencia
		System.out.println(c);
		
		c = "modificando variavel, texto por inferencia";
		System.out.println(c);
		
	}

}
