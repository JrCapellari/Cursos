package poo.composicao;

import java.util.ArrayList;
import java.util.List;

public class Curso {
    // Atributos
    final String nome;
    final List<Aluno> alunos = new ArrayList<>();

    // Metodos
    Curso(String nome){
        this.nome = nome;
    }

    void adicionarAluno(Aluno aluno){
        this.alunos.add(aluno);
        aluno.cursos.add(this);
    }
}
