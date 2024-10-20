package teste.basico;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import modelo.basico.Usuario;

public class AlterarUsuario3 {
    public static void main(String[] args) {
        
        // OBJETO LIVRE DO ESTADO GERENCIADO NÃO FAZ UPDATE

        EntityManagerFactory emf = Persistence.
            createEntityManagerFactory("exercicios-jpa");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();

        Usuario usuario = em.find(Usuario.class, 6L);

        // COMADO DETACH LIBERA DO ESTADO GERENCIADO
        em.detach(usuario);

        usuario.setNome("Leonardo");
        //usuario.setEmail("leonardo@lanche.com.br");

        // UPDATE NECESSITA DO COMANDO MERGE
        em.merge(usuario); 
        em.getTransaction().commit();

        em.close();
        emf.close();
    }

}
