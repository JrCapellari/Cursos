package poo.heranca.desafio;

public class Ferrari extends Carro implements Esportivo, Luxo {
    
    boolean ligarTurbo;
    boolean ligarAr;

    //Construtor
    public Ferrari(int velocidadeMaxima){
        super(velocidadeMaxima);
        setDelta(20);
    }
    @Override
    public void ligarTurbo() {
        ligarTurbo = true;
    }
    @Override
    public void desligarTurbo() {
        ligarTurbo = false;
        
    }
    @Override
    public void ligarAr() {
        ligarAr = true;
        
    }
    @Override
    public void desligarAr() {
        ligarAr = false;
        
    }
    @Override
    public int getDelta() {
        if (ligarTurbo && !ligarAr) {
            return 40;
        }else if (ligarTurbo && ligarAr) {
            return 30;
        }else if (!ligarTurbo && ligarAr) {
            return 15;
        }else {
            return 20;
        }
    }
}
