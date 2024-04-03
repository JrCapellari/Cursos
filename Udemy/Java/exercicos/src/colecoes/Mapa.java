package colecoes;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Mapa {

    public static void main(String[] args) {
        
        Map<Integer, String> usuarios = new HashMap<>();

        usuarios.put(1, "Roberto"); // Inseri e substitui
        usuarios.put(1, "Ricardo");
        usuarios.put(2, "Rafaela");
        usuarios.put(3, "Rebeca");
        usuarios.put(4, "Rosali");
        usuarios.put(5, "Leandro");
        
        System.out.println("Tamanho: " + usuarios.size());
        System.out.println("Chaves: " + usuarios.keySet());
        System.out.println("Valores: " + usuarios.values());
        System.out.println("Chave/Valor: " + usuarios.entrySet());

        System.out.println("Existe a chave: " + usuarios.containsKey(3));
        System.out.println("Existe o valor: " + usuarios.containsValue("Rebeca"));

        System.out.println(usuarios.get(3));
        System.out.println(usuarios.remove(1));
        System.out.println(usuarios.remove(2, "Junior"));

        for (Integer chave : usuarios.keySet()) {
            System.out.println(chave);
            
        }
        for (String valor : usuarios.values()) {
            System.out.println(valor);
            
        }
        for (Entry<Integer, String> registro : usuarios.entrySet()){
            System.out.println(registro);
            System.out.println(registro.getKey());
            System.out.println(registro.getValue());
        }
    }
}
