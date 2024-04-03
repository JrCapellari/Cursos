package colecoes;

import java.util.ArrayDeque;
import java.util.Deque;

public class Pilha {
    public static void main(String[] args) {
        
        // Pilha - FILO
        Deque<String> livros = new ArrayDeque<>();

        livros.add("O pequeno Principe"); // false caso pilha cheia
        livros.push("Dom Quixote"); // gera exceção caso pilha cheia
        livros.push("O Hobbit");

        System.out.println(livros.isEmpty()); // esta vazia?

        System.out.println(livros.peek());// false caso pilha cheia
        System.out.println(livros.element());// gera exceção caso pilha cheia

        System.out.println(livros.poll()); // fila vazia - retorna null
        System.out.println(livros.remove()); // fila vazia - gera uma exceção

        //livros.size
        //livros.clear
        //livros.contains
    }
}
