package generics;

public class Caixa<T> {
    private T coisa;

    // set
    public void guardar(T coisa) {
        this.coisa = coisa;
    }

    // get
    public T abrir() {
        return coisa;
    }

}
