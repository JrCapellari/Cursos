package classe;

public class DataTeste {
    public static void main(String[] args) {
        Data nascimento = new Data();
        nascimento.dia = 1;
        nascimento.mes = 6;
        nascimento.ano = 1978;

        Data nascimento2 = new Data(18, 3, 1981);

        Data nascimento3 = new Data(); // recebe o setado no construtor padrão

        System.out.printf("Nascimento: %d/%d/%d\n", nascimento.dia, nascimento.mes, nascimento.ano);
        System.out.printf("Nascimento: %s\n", nascimento.dataFormatada());
        nascimento.imprimirDataFormatada();
        System.out.println("\n----------------------");
        nascimento2.imprimirDataFormatada();
        System.out.println("\n----------------------");
        nascimento3.imprimirDataFormatada();


    }
}
