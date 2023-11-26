package classe;

public class Data {
// Atributos
    int dia;
    int mes;
    int ano;

// Construtor
    // Construtor Padrão
    Data(){
        // dia = 1;
        // mes = 1;
        // ano = 1970;
        this(1, 1, 1970);
    }
    // Construtor com parametros
    Data(int dia, int mes, int ano ){
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

// Metodos
    // Forma correta (usando return)
    String dataFormatada(){
        // return dia + "/" + mes + "/" + ano;
        return String.format("%d/%d/%d", dia, mes, ano); // Usando metodo String.format
    }
    // Funciona apenas em terminal (usando SOUT)
    void imprimirDataFormatada(){
        System.out.print("Nascimento: " + dataFormatada()); // Chamando outro metodo
    }
}
