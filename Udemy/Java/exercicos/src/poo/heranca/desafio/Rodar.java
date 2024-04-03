package poo.heranca.desafio;

public class Rodar {
    public static void main(String[] args) {
        Fusca fusca = new Fusca(80);
        fusca.acelerar();
        fusca.acelerar();
        fusca.acelerar();
        fusca.acelerar();
        fusca.acelerar();
        fusca.frear();
        fusca.frear();
        fusca.acelerar();
        fusca.acelerar();
        fusca.acelerar();

        System.out.println(fusca);

        Ferrari ferrari = new Ferrari(200);
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();  // aqui deveria ser 220Km/h
        

        System.out.println(ferrari);
    }
}
