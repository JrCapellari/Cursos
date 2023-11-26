package controle;

public class WhileDeterminado {
    public static void main(String[] args) {

        double contador = 0;
        while(contador <= 2.0 ){
            System.out.printf("numero %f\n", contador);
            contador = contador + 0.111111;
        }
    }
}
