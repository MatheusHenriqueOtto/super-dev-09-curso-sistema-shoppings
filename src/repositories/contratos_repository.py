from typing import Any
from src.database.conexao import conectar
from src.schemas.contratos import Contrato, ContratoCadastro, ContratoEditar


def consultar_todos() -> list[Contrato]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, data_inicio, data_fim, valor_aluguel, id_loja, id_shopping,
                CAST(registro_ativo AS UNSIGNED) FROM contratos WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Contrato(registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], bool(registro[6])) for registro in registros]


def consultar_por_id(id: int) -> Contrato | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, data_inicio, data_fim, valor_aluguel, id_loja, id_shopping, CAST(registro_ativo AS UNSIGNED) 
                FROM contratos 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()
            
    if registro is None:
        return None
        
    return Contrato(
        registro[0],
        registro[1],
        registro[2],
        float(registro[3]),
        registro[4],
        registro[5],
        bool(registro[6])
    )



def cadastrar(item: ContratoCadastro) -> Contrato:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO contratos (data_inicio, data_fim, valor_aluguel, id_loja, id_shopping, registro_ativo) VALUES (%s, %s, %s, %s, %s, 1)", (item.data_inicio, item.data_fim, item.valor_aluguel, item.id_loja, item.id_shopping))
            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)
            
            else:
                raise ValueError("Falha ao obter o ID do contrato cadastrado.")
            
        conexao.commit()
    return Contrato(novo_id, item.data_inicio, item.data_fim, item.valor_aluguel, item.id_loja, item.id_shopping, True)


def atualizar(id: int, item: ContratoEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE contratos SET data_inicio = %s, data_fim = %s, valor_aluguel = %s, id_loja = %s, id_shopping = %s WHERE id = %s", (item.data_inicio, item.data_fim, item.valor_aluguel, item.id_loja, item.id_shopping, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM contratos WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE contratos SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM contratos WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
