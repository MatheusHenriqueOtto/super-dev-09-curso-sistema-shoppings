from typing import Any
from src.database.conexao import conectar
from src.schemas.estacionamento import Estacionamento, EstacionamentoCadastro, EstacionamentoEditar


def consultar_todos() -> list[Estacionamento]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, setor, capacidade_vagas, id_shopping, CAST(registro_ativo AS UNSIGNED)
                FROM estacionamento WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Estacionamento(registro[0], registro[1], registro[2], registro[3], bool(registro[4])) for registro in registros]


def consultar_por_id(id: int) -> Estacionamento | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, setor, capacidade_vagas, id_shopping, CAST(registro_ativo AS UNSIGNED)
                FROM estacionamento 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()
            
    if registro is None:
        return None
        
    return Estacionamento(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        bool(registro[4])
    )



def cadastrar(item: EstacionamentoCadastro) -> Estacionamento:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO estacionamento (setor, capacidade_vagas, id_shopping, registro_ativo) VALUES (%s, %s, %s, 1)", (item.setor, item.capacidade_vagas, item.id_shopping))
            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)
            
            else:
                raise ValueError("Falha ao obter o ID do estacionamento cadastrado.")
            
        conexao.commit()
    return Estacionamento(novo_id, item.setor, item.capacidade_vagas, item.id_shopping, True)


def atualizar(id: int, item: EstacionamentoEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE estacionamento SET setor = %s, capacidade_vagas = %s, id_shopping = %s WHERE id = %s", (item.setor, item.capacidade_vagas, item.id_shopping, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM estacionamento WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE estacionamento SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM estacionamento WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
