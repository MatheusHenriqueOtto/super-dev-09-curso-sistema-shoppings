from typing import Any
from src.database.conexao import conectar
from src.schemas.avaliacoes import Avaliacao, AvaliacaoCadastro, AvaliacaoEditar


def consultar_todos() -> list[Avaliacao]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, nota, comentario, id_cliente, CAST(registro_ativo AS UNSIGNED)
                FROM avaliacoes WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Avaliacao(registro[0], registro[1], registro[2], registro[3], bool(registro[4])) for registro in registros]


def consultar_por_id(id: int) -> Avaliacao | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nota, comentario, id_cliente, CAST(registro_ativo AS UNSIGNED)
                FROM avaliacoes 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()

    if registro is None:
        return None

    return Avaliacao(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        bool(registro[4])
    )


def cadastrar(item: AvaliacaoCadastro) -> Avaliacao:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO avaliacoes (nota, comentario, id_cliente, registro_ativo) VALUES (%s, %s, %s, 1)", (item.nota, item.comentario, item.id_cliente))
            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)
            
            else:
                raise ValueError("Falha ao obter o ID da avaliacão cadastrada.")
            
        conexao.commit()
    return Avaliacao(novo_id, item.nota, item.comentario, item.id_cliente, True)


def atualizar(id: int, item: AvaliacaoEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE avaliacoes SET nota = %s, comentario = %s, id_cliente = %s WHERE id = %s", (item.nota, item.comentario, item.id_cliente, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM avaliacoes WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE avaliacoes SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM avaliacoes WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
