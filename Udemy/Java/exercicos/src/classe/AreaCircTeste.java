package classe;

public class AreaCircTeste {
    public static void main(String[] args) {
        AreaCirc a = new AreaCirc(5.6);
        System.out.println("Area = " + a.area());
        System.out.println("PI = " + AreaCirc.PI);
        System.out.println("PI da API Java = " + Math.PI);
        System.out.println("Area Static = " + AreaCirc.area(100));
    }
}
