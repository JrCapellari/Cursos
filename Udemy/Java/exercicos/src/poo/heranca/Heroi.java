package poo.heranca;

public class Heroi extends Jogador {

    //Construtor
    public Heroi(int x, int y){
        super(x, y);
    }

    //Metodos
    @Override
    public boolean atacar(Jogador oponente) {
        boolean ataque1 = super.atacar(oponente);
        boolean ataque2 = super.atacar(oponente);
        return (ataque1 || ataque2);
    }
}
