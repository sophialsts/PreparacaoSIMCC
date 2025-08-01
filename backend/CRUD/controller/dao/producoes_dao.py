# Importa a conexão Singleton do banco de dados
from banco import conexao_singleton as cs

# Obtém uma instância de conexão com o banco de dados
conexao = cs.Conexao().get_conexao()

def verificar_id_pesquisador(pesquisadores_id: str):
        sql2 = """
            SELECT * FROM pesquisadores
            WHERE pesquisadores_id = %s
        """
        
        with conexao.cursor() as cursor:
            cursor.execute(sql2, (pesquisadores_id,))
            resultado = cursor.fetchone()  
        
        return resultado is not None  

# Função para salvar um nova producao no banco de dados
def salvar_nova_producao(producoes_id: str, pesquisadores_id: str, issn: str, nomeartigo: str, anoartigo: int ) -> str:
    
    if not verificar_id_pesquisador(pesquisadores_id):
        return "Erro: Pesquisador não encontrado"

    # SQL para inserir um novo registro na tabela "producoes"
    sql = """
            INSERT INTO producoes (producoes_id, pesquisadores_id, issn, nomeartigo, anoartigo)
            VALUES (%s, %s, %s, %s, %s)
        """
    
    try:
        # Utiliza a conexão para abrir um cursor e executar o SQL
        with conexao.cursor() as cursor:
            cursor.execute(sql, (producoes_id, pesquisadores_id, issn, nomeartigo, anoartigo))
            # Confirma a transação no banco
            conexao.commit()
            
            return "Nova produção salva com sucesso!"
    except Exception as e:
        # Se ocorrer uma exceção, reverte a transação
        conexao.rollback()
        return f"Erro ao salvar: {e}"
    
# Função para listar todos os producoes do banco de dados
def listar_todas() -> str:
    # SQL para selecionar todos os registros da tabela "producoes"
    sql: str = "SELECT * FROM producoes;"
    
    # Utiliza a conexão para abrir um cursor e executar o SQL
    with conexao.cursor() as cursor:
        cursor.execute(sql)
        # Obtém todos os resultados da consulta
        resultado = cursor.fetchall()
        
        # Cria uma lista das colunas retornadas pela consulta
        colunas = [desc[0] for desc in cursor.description]
        # Mapeia os resultados em dicionários com chave-valor
        dados = [dict(zip(colunas, linha)) for linha in resultado]
        
        return dados

# Função para atualizar uma produção no banco de dados com base no "producoes_id"
def atualizar_por_id(nomeartigo: str, issn: str, pesquisadores_id: str, anoartigo: str, producoes_id: str) -> str:
    # SQL para atualizar os dados de uma produção específica
    sql = """
            UPDATE producoes
            SET nomeartigo = %s, issn = %s, pesquisadores_id = %s, anoartigo = %s
            WHERE producoes_id = %s
        """
    
    try:
        # Utiliza a conexão para abrir um cursor e executar o SQL
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nomeartigo, issn, pesquisadores_id, anoartigo, producoes_id))
            
            if (cursor.rowcount < 0):
                raise Exception()
            
            # Confirma a transação no banco
            conexao.commit()
            
            return "Produção atualizada com sucesso!"
    except Exception as e:
        # Se ocorrer uma exceção, reverte a transação
        conexao.rollback()
        return f"Erro ao atualizar produção: {e}"

# Função para apagar uma produção do banco de dados com base no "producoes_id"
def apagar_por_producoes_id(producoes_id: str) -> str:
    
    # SQL para excluir uma produção específico com base no "producoes_id"

    sql = """
            DELETE FROM producoes
            WHERE producoes_id = %s
        """
    
    try:
        # Utiliza a conexão para abrir um cursor e executar o SQL
        with conexao.cursor() as cursor:
            
            cursor.execute(sql, (producoes_id,))
            
            if (cursor.rowcount > 0):
                # Confirma a transação no banco
                conexao.commit()
            else:
                raise Exception()
            
            return "Produção apagada com sucesso!"
    except Exception as e:
        # Se ocorrer uma exceção, reverte a transação
        conexao.rollback()
        return f"Erro ao apagar produção. Produção inexistente ou ID inválido."
    