package poo.heranca;

public class Jogo {
    public static void main(String[] args) {
        Monstro monstro = new Monstro(10,10);

        Heroi heroi = new Heroi(10 ,11);
        
        System.out.println("Vida Monstro: " + monstro.vida);
        System.out.println("Vida Heroi: " + heroi.vida);

        monstro.atacar (heroi);
        heroi.atacar(monstro);
        monstro.atacar (heroi);
        heroi.atacar(monstro);

        monstro.andar(Direcao.norte);

        monstro.atacar (heroi);
        heroi.atacar(monstro);

        System.out.println("Vida Monstro: " + monstro.vida);
        System.out.println("Vida Heroi: " + heroi.vida);

    }

}
