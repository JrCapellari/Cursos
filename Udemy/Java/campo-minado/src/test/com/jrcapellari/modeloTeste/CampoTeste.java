package test.com.jrcapellari.modeloTeste;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.Test;
import org.junit.jupiter.api.BeforeEach;

import main.com.jrcapellari.excecao.ExplosaoException;
import main.com.jrcapellari.modelo.Campo;


public class CampoTeste {
    private Campo campo;

    @BeforeEach
    void iniciarCampo() {
        campo = new Campo(3, 3);
    }
    @Test
    public void testeVizinhoDistancia1Esqueda() {
        Campo vizinho = new Campo(3, 2);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertTrue(resultado);
    }
    @Test
    public void testeVizinhoDistancia1Direita() {
        Campo vizinho = new Campo(3, 4);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertTrue(resultado);
    }
    @Test
    public void testeVizinhoDistancia1EmCima() {
        Campo vizinho = new Campo(2, 3);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertTrue(resultado);
    }
    @Test
    public void testeVizinhoDistancia1EmBaixo() {
        Campo vizinho = new Campo(4, 3);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertTrue(resultado);
    }
    @Test
    public void testeVizinhoDistancia2() {
        Campo vizinho = new Campo(2, 2);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertTrue(resultado);
    }
    @Test
    public void testeNaoVizinho() {
        Campo vizinho = new Campo(1, 1);
        boolean resultado = campo.adicionaVizinho(vizinho);
        assertFalse(resultado);
    }
    @Test
    public void testeValorPadraoAtributoMarcado() {
        assertFalse(campo.isMarcado());
    }
    @Test
    public void testeAlternarMarcacao() {
        campo.alternarMarcacao();
        assertTrue(campo.isMarcado());
    }
    @Test
    public void testeAlternarMarcacaoDuasChamadas() {
        campo.alternarMarcacao();
        campo.alternarMarcacao();
        assertFalse(campo.isMarcado());
    }
    @Test
    public void testeAbrirNaoMinadoNaoMarcado() {
        assertTrue(campo.abrir());
    }
    @Test
    public void testeAbrirNaoMinadoMarcado() {
        campo.alternarMarcacao();
        assertFalse(campo.abrir());
    }
    @Test
    public void testeAbrirMinadoMarcado() {
        campo.alternarMarcacao();
        campo.minar();
        assertFalse(campo.abrir());
    }
    @Test
    public void testeAbrirMinadoNaoMarcado() {
        campo.minar();
        assertThrows(ExplosaoException.class, () -> {campo.abrir();});
    }
    @Test
    public void testeAbrirComVizinhos1() {
        Campo campo11 = new Campo(1, 1);

        Campo campo22 = new Campo(2,2);
        campo22.adicionaVizinho(campo11);

        campo.adicionaVizinho(campo22);
        campo.abrir();

        assertTrue(campo22.isAberto() && campo11.isAberto());
    }
    @Test
    public void testeAbrirComVizinhos2() {
        Campo campo11 = new Campo(1, 1);
        Campo campo12 = new Campo(1, 1);
        campo12.minar();

        Campo campo22 = new Campo(2,2);
        campo22.adicionaVizinho(campo11);
        campo22.adicionaVizinho(campo12);

        campo.adicionaVizinho(campo22);
        campo.abrir();

        assertTrue(campo22.isAberto() && campo11.isFechado());
    }    
}
