package teste.basico;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import modelo.basico.Usuario;

public class AlterarUsuario2 {
    public static void main(String[] args) {
        
        // OBJETO NO ESTADO GERENCIADO SEMPRE FARA UPDATE

        EntityManagerFactory emf = Persistence.
            createEntityManagerFactory("exercicios-jpa");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();

        Usuario usuario = em.find(Usuario.class, 6L);
        usuario.setNome("Leonardo Leitão");
        //usuario.setEmail("leonardo@lanche.com.br");

        // UPDATE MESMO SEM COMANDO MERGE
        //em.merge(usuario); 
        em.getTransaction().commit();

        em.close();
        emf.close();
    }

}
