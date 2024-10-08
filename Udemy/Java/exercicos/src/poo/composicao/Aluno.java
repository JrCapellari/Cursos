package poo.composicao;

import java.util.ArrayList;
import java.util.List;

public class Aluno {
    // Atributos
    final String nome;
    final List<Curso> cursos = new ArrayList<>();

    // Metodos
    Aluno(String nome){
        this.nome = nome;
    }

    void adicionarCurso(Curso curso){
        this.cursos.add(curso);
        curso.alunos.add(this);
    }

    public String toString(){
        return nome;
    }

    Curso obterCursoPorNome(String nome){
        for (Curso curso : this.cursos) {
            if (curso.nome.equalsIgnoreCase(nome)) {
                return curso;
            }
        }
        return null;
    }
}
