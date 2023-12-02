package classe.desafio;

public class Pessoa {
    //Atributos
    String nome;
    Double peso;

    //Construtor
    Pessoa(String nome, Double peso){
        this.nome = nome;
        this.peso = peso;
    }
    //Metodos
    void comer(Comida comida){
        if(comida != null){
            this.peso += comida.peso;
        }
    }
    String apresentar(){
        return nome + " tem " + peso + "Kg";
    }
    
}
