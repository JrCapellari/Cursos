package fundamentos;

import javax.swing.*;

public class DesafioCalculadora {
    public static void main(String[] args) {
        //num1
        //num2
        //op + - * / %

        double num1 = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro numero:"));
        double num2 = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo numero:"));

        String op = JOptionPane.showInputDialog("Digite um operador + - * / %:");
        double res = "+".equals(op) ? num1 + num2 : 0;
        res = "-".equals(op) ? num1 - num2 : res;
        res = "*".equals(op) ? num1 * num2 : res;
        res = "/".equals(op) ? num1 / num2 : res;
        res = "%".equals(op) ? num1 % num2 : res;
        System.out.printf("Resultado: %.2f %s %.2f = %.2f", num1, op, num2, res);


    }
}
