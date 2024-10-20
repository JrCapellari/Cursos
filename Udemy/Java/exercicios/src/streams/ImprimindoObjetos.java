package streams;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Stream;

public class ImprimindoObjetos {
    public static void main(String[] args) {
        
        List<String> aprovados = Arrays.asList("Lu", "Gui", "Luca", "Ana");

        // For tradicional
        System.out.println("Usando For Tradicional");
        for (int i = 0; i < aprovados.size(); i++) {
            System.out.println(aprovados.get(i));
        }
        // For Each
        System.out.println("\nUsando For Each");
        for (String nome : aprovados) {
            System.out.println(nome);
        }
        // Iterator
        System.out.println("\nUsando Iterator");
        Iterator<String> iteracao = aprovados.iterator();
        while (iteracao.hasNext()) {
            System.out.println(iteracao.next());
            
        }
        // Stream
        System.out.println("\nUsando Stream");
        Stream<String> fluxo = aprovados.stream();
        fluxo.forEach(System.out::println); // laço Interno
    }
}
