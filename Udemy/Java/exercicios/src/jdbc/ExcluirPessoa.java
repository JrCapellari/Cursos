package jdbc;


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

public class ExcluirPessoa {
    public static void main(String[] args) throws SQLException{

        Scanner entrada = new Scanner(System.in);
        System.out.print("Informe o código: ");
        int codigo = entrada.nextInt();

        Connection conexao = FabricaConexao.getConexao();
        String deleteSQL = "DELETE FROM pessoas WHERE codigo = ?";

        PreparedStatement stmt = conexao.prepareStatement(deleteSQL);
        stmt.setInt(1, codigo);

        int contador = stmt.executeUpdate();

        if (contador > 0) {
            System.out.println("Pessoa excluida");
        }else {
            System.out.println("Operação não relaizada");
        }

        System.out.println("Linhas afetadas: " + contador);
        
        conexao.close();
        entrada.close();
    }

}
