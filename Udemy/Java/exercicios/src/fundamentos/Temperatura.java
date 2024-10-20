package fundamentos;

public class Temperatura {
	public static void main(String[] args) {
		final int N = 32;
		final double D = 5.0/9.0;
		double f = 86;
		double c = (f - N) * D;
		System.out.println("A temperatura em Fahrenheit e " + f + "f");
		System.out.println("A temperatura em celsius e: " + c + "c");
		System.out.println("-------------------------------------");
		
	}

}
