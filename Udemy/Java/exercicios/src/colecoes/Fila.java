package colecoes;

import java.util.LinkedList;
import java.util.Queue;

public class Fila {
    public static void main(String[] args) {

        // Fila - FIFO
        Queue<String> fila = new LinkedList<>();

        // Inserem elementos
        fila.add("Ana"); // retorna false se fila cheia
        fila.offer("Bia"); // gera exceção se fila cheia
        fila.offer("Carlos"); 
        fila.offer("Daniel"); 
        fila.offer("Rafaela"); 
        fila.offer("Gui");

        System.out.println(fila.isEmpty()); // esta vazia?
        
        // não remove o elemento
        System.out.println(fila.peek()); // fila vazia - retorna null
        System.out.println(fila.element());// fila vazia - gera uma exceção

        // remove o elemento
        System.out.println(fila.poll()); // fila vazia - retorna null
        System.out.println(fila.remove()); // fila vazia - gera uma exceção

        //fila.size
        //fila.clear
        //fila.contains

    }
}
