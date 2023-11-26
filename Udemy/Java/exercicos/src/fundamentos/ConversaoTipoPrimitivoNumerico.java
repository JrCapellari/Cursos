package fundamentos;

public class ConversaoTipoPrimitivoNumerico {
	public static void main(String[] args) {
		
		double a = 1; // conversão implicita
		System.out.println(a);
		
		float b = (float) 1.523; //conversão explicita (cast)
		System.out.println(b);
		
		int c = 127;
		byte d = (byte) c; //conversão explicita (cast)
		System.out.println(d);
		
		double e = 1.988;
		int f = (int) e; //conversão explicita (cast)
		System.out.println(f);
	}

}
