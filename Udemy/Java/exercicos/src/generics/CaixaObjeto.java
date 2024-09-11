package generics;

public class CaixaObjeto {

    private Object coisa;

    // set
    public void guardar(Object coisa) {
        this.coisa = coisa;
    }

    // get
    public Object abrir() {
        return coisa;
    }

}
