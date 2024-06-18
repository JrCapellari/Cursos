package main.com.jrcapellari;

import main.com.jrcapellari.modelo.Tabuleiro;
import main.com.jrcapellari.visao.TabuleiroConsole;

public class Aplicacao {
    public static void main(String[] args) {
        
        Tabuleiro tabuleiro = new Tabuleiro(6, 6, 3);
        new TabuleiroConsole(tabuleiro);

    }

}
