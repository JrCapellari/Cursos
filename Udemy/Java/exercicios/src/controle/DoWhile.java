package controle;

import java.util.Scanner;

public class DoWhile {
    public static void main(String[] args) {
        // if(condição) sentença ou {bloco}
        // while(condição) sentença ou {bloco}
        // for(variavel; condição; incremento) sentença ou {bloco}
        // do sentença ou {bloco} while(condição)

        Scanner entrada = new Scanner(System.in);
        String texto = "";
        do{
            System.out.println("Escreva as palavras magicas: ");
            System.out.print("Quer sair: ");
            texto = entrada.nextLine();
        }while(!texto.equalsIgnoreCase("por favor"));
        System.out.println("Obrigado");

        entrada.close();
    }
}
