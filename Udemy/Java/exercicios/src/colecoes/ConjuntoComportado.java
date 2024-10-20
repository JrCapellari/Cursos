package colecoes;

import java.util.Set;
import java.util.TreeSet;

public class ConjuntoComportado {
    public static void main(String[] args) {
        
        //Set<String> lista = new HashSet<>();
        Set<String> lista = new TreeSet<>();
        lista.add("Ana");
        lista.add("Carlos");
        lista.add("Luca");
        lista.add("Pedro");

        //System.out.println(lista);
        System.out.println("Há " + lista.size() + " elementos no conjunto");

        for (String nomes : lista) {
            System.out.println(nomes);
        }

        Set<Integer> nums = new TreeSet<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);

        for (Integer number : nums) {
            System.out.println(number);
            
        }
    }
}
