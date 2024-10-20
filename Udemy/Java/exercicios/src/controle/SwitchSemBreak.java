package controle;

public class SwitchSemBreak {
    public static void main(String[] args) {
        String faixa = "preta";
        System.out.printf("A faixa %s deve saber\n", faixa);
        switch (faixa.toLowerCase()) {
            case"preta":
                System.out.println("Bassai-Dai");
            case"marrom":
                System.out.println("Tekki Shodan");
            case"roxa":
                System.out.println("Heian Godan");
            case"verde":
                System.out.println("Heian Yodan");
            case"laranja":
                System.out.println("Heian Sandan");
            case"vermelha":
                System.out.println("Heian Nidan");
            case"amarela":
                System.out.println("Heian Shodan");
                break;
            default:
                System.out.println("Iniciante");
        }
    }
}
