package poo.encapsulamento;

public class Pessoa {

    //Atributos
    private String nome;
    private int Idade;

    // Construtor
    public Pessoa (String nome, int idade){
        setNome(nome);
        setIdade(idade);
    }

    // Metodos
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getIdade() {
        return Idade;
    }
    public void setIdade(int novaIdade) {
        novaIdade = Math.abs(novaIdade);
        if (novaIdade >= 0 && novaIdade < 120) {
            this.Idade = novaIdade;
            
        }
    }
    @Override
    public String toString() {
        return "Nome: " + getNome() + " - Idade: " + getIdade() + "anos";
    }
}
