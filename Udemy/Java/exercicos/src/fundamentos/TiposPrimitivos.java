package fundamentos;

public class TiposPrimitivos {
	public static void main(String[] args) {
		// Tipos numéricos inteiros
		byte anosDeEmpresa = 23;
		short numeroDeVoos = 542;
		int id = 56789;
		long pontosAcumulados = 3234845223L;
		
		//Tipos numéricos reais
		float salario = 11445.44f;
		double vendasAcumuladas = 2991797103.01;
		
		//Tipo booleano
		boolean estaDeFerias = false; //true
				
		//Tipo caractere
		char status = 'A'; //Ativo
		
		//Dias de empresa
		System.out.println(anosDeEmpresa * 365);
		
		//Numeros de viagens
		System.out.println(numeroDeVoos / 2);
		
		//Pontos por real
		System.out.println(pontosAcumulados / vendasAcumuladas);
		
		//id
		System.out.println("ID: " + id + " ganha " + salario);
		
		//Esta de ferias
		System.out.println("Ferias? " + estaDeFerias);
		
		//Status
		System.out.println("Status: " + status);
		
	}

}
