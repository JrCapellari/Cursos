import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="pandora", host="127.0.0.1", port="5432")
print('Conexão com Banco de Dados efetuada')
cur = conn.cursor()
#  CRIA A TABELA NO BANCO ------------------------------------------------------------------------------------
#  cur.execute('''CREATE TABLE agenda(ID INT PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12));''')
#  print('Tabela criada com sucesso')
#  INSERE DADOS NA TABELA ------------------------------------------------------------------------------------
#  cur.execute('''INSERT INTO "agenda"("id", "nome", "telefone") VALUES (1, 'Pessoa1', '51999999999')''')
#  print('Dados inseridos com sucesso')
#  SELECIONA UM REGISTRO NA TABELA ---------------------------------------------------------------------------
#  print('Consulta antes da atualização')
#  cur.execute('''SELECT * FROM "agenda" WHERE "id"=1''')
#  registro = cur.fetchone()
#  print(registro)
#  ATUALIZAÇÃO DE UM ÚNICO REGISTRO --------------------------------------------------------------------------
#  cur.execute('''UPDATE "agenda" SET "telefone"='51988888888' WHERE "id"=1''')
#  conn.commit()
#  print('Registro atualizado com sucesso')
#  cur = conn.cursor()
#  print('Consulta apos atualização')
#  cur.execute('''SELECT * FROM "agenda" WHERE "id"=1''')
#  registro = cur.fetchone()
#  print(registro)
#  EXCLUSÃO DE DADOS NA TABELA ------------------------------------------------------------------------------
cur.execute('''DELETE FROM "agenda" WHERE "id"=1''')
conn.commit()
cont = cur.rowcount
print(cont, "Registro excluído")
#  print('Seleção realizada com sucesso')
conn.close()
print('Conexão encerrada')
