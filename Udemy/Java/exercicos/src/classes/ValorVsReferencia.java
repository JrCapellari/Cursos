package classes;

public class ValorVsReferencia {
    public static void main(String[] args) {
        double a = 2;
        double b = a; // Atribuição por valor

        a++;
        b--;
        System.out.println(a + "\n" + b);

        Data d1 = new Data(1, 1, 1970);
        Data d2 = d1; // Atribuição por referencia (objeto)

        d1.dia = 31;
        d2.mes = 12;
        System.out.println(d1.dataFormatada());
        System.out.println(d2.dataFormatada());

        voltaDataPadrao(d1);
        System.out.println(d1.dataFormatada());
        System.out.println(d2.dataFormatada());

        int c = 5;
        alterarPrimitivo(c);
        System.out.println(c);
    }
    static void voltaDataPadrao(Data d){
        d.dia = 1;
        d.mes = 1 ;
        d.ano = 1970;
    }
    static void alterarPrimitivo(int a){
        a++;
    }
}
