package controle;

public class ContinueRotulado {
    public static void main(String[] args) {
        externo: for(int i = 0; i < 3; i++){ // externo é rotulo
            interno: for(int j = 0; j < 3; j++){ // interno é rotulo
                if(i == 1){
                    continue externo;
                }
                System.out.printf(" [%d %d]", i, j);
            }
            System.out.println();
        }
        System.out.println("FIM");
    }
}
