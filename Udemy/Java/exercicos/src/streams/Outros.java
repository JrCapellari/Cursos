package streams;

import java.util.Arrays;
import java.util.List;

public class Outros {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("João", 7.3);
        Aluno a2 = new Aluno("Ana", 8.7);
        Aluno a3 = new Aluno("Pedro", 5.9);
        Aluno a4 = new Aluno("Gabi", 6.7);
        Aluno a5 = new Aluno("João", 7.3);
        Aluno a6 = new Aluno("Maria", 6.9);
        Aluno a7 = new Aluno("Pedro", 5.9);
        Aluno a8 = new Aluno("Cris", 5.2);
        // Aluno a5 = new Aluno("Miguel", 4.1);
        // Aluno a6 = new Aluno("Julia", 7.7);
        // Aluno a7 = new Aluno("Maria", 6.9);
        // Aluno a8 = new Aluno("Cris", 5.2);

        List<Aluno> alunos = Arrays.asList(a1, a2, a3, a4, a5, a6, a7, a8);
        
        // distinct
        System.out.println("distinct ------");
        alunos.stream().distinct().forEach(System.out::println);

        // skip/limit
        System.out.println("\nskip/limit ------");
        alunos.stream()
        .distinct()
        .skip(02)
        .limit(2)
        .forEach(System.out::println);

        // takeWhile
        System.out.println("\ntakeWhile ------");
        alunos.stream()
        .distinct()
        .takeWhile(a -> a.nota >= 7)
        .forEach(System.out::println);
        
        
    }

}
