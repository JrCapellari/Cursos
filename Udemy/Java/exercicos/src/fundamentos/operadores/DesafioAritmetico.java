package fundamentos.operadores;

public class DesafioAritmetico {
	public static void main(String[] args) {
		
		// Dicas
		//int a = 3 * 4 - 10;
		//int b = (int) Math.pow(a, 3);
		//double c = Math.pow(a, 3);
		
		//System.out.println(b);
		//System.out.println(c);
		
		//Desafio
		double numA = Math.pow(6 * (3 + 2), 2);
		double denA = 3 * 2;
		
		double numB = (1 -5) * (2 - 7);
		double denB = 2;
		
		double supA = numA / denA;
		double supB = Math.pow(numB / denB, 2);
		
		double sup = Math.pow(supA - supB, 3);
		double inf = Math.pow(10, 3);
		
		double res = sup / inf;
		
		System.out.println(res);
		
		
		
		
		
	}

}
