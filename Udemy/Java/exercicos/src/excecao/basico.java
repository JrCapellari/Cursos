package excecao;

public class basico {
    public static void main(String[] args) {
        
        Aluno a1 = null;

        try {
            imprimirNomeDoAluno(a1);

        }catch(Exception execao) {
            System.out.println("Ocorreu um erro ao imprimir aluno");
        }
       
        try {
            System.out.println(7 / 0);

        } catch (ArithmeticException e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }

        System.out.println("FIM");
    }
    public static void imprimirNomeDoAluno(Aluno aluno) {
        System.out.println(aluno.nome);
    }

}
