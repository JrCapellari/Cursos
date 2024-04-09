package poo.heranca.teste;

import poo.heranca.desafio.Ferrari;
import poo.heranca.desafio.Fusca;

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

        Ferrari ferrari = new Ferrari (200);
        ferrari.ligarTurbo();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.acelerar();
        ferrari.frear();
        ferrari.frear();
        ferrari.desligarTurbo();
        ferrari.acelerar();


        System.out.println(ferrari);
    }
}
