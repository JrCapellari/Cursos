package fundamentos;

public class NotacaoPonto {
	public static void main(String[] args) {
		
		String s = "Bom dia Mundo";
		s = s.replace("Mundo", "para todos");
		s = s.toUpperCase();
		s = s.concat("!!!");
		
		System.out.println(s);
		
		System.out.println("junior".toUpperCase());
		String x = "junior".toUpperCase();
		System.out.println(x);
		
		String y = "Bom dia X"
				.replace("X", "Junior")
				.toUpperCase()
				.concat("!!!");
		System.out.println(y);
		
		//Tipos primitivos não tem operador ponto
	}

}
