from src.database.conexao import conectar
from src.schemas.avaliacoes import Avaliacao


# =========================
# LISTAR TODOS
# =========================

def consultar_todos() -> list[Avaliacao]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nota, comentario, id_cliente, registro_ativo
                FROM avaliacoes
            """)

            registros = cursor.fetchall()

    avaliacoes = []

    for registro in registros:
        avaliacao = Avaliacao(
            id=registro[0],
            nota=registro[1],
            comentario=registro[2],
            id_cliente=registro[3],
            registro_ativo=registro[4]
        )

        avaliacoes.append(avaliacao)

    return avaliacoes


# =========================
# BUSCAR POR ID
# =========================

def consultar_por_id(id_avaliacao: int) -> Avaliacao | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nota, comentario, id_cliente, registro_ativo
                FROM avaliacoes
                WHERE id = %s
            """, (id_avaliacao,))

            registro = cursor.fetchone()

    if registro is None:
        return None

    return Avaliacao(
        id=registro[0],
        nota=registro[1],
        comentario=registro[2],
        id_cliente=registro[3],
        registro_ativo=registro[4]
    )


# =========================
# CADASTRAR
# =========================

def cadastrar(
    nota: int,
    comentario: str | None,
    id_cliente: int
) -> None:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                INSERT INTO avaliacoes
                (nota, comentario, id_cliente, registro_ativo)
                VALUES (%s, %s, %s, 1)
            """, (nota, comentario, id_cliente))

        conexao.commit()


# =========================
# ATUALIZAR
# =========================

def atualizar(
    id_avaliacao: int,
    nota: int,
    comentario: str | None,
    id_cliente: int
) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE avaliacoes
                SET nota = %s,
                    comentario = %s,
                    id_cliente = %s
                WHERE id = %s
            """, (
                nota,
                comentario,
                id_cliente,
                id_avaliacao
            ))

            alterados = cursor.rowcount

        conexao.commit()

    return alterados > 0


# =========================
# ALTERAR STATUS
# =========================

def alterar_status(
    id_avaliacao: int,
    registro_ativo: bool
) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE avaliacoes
                SET registro_ativo = %s
                WHERE id = %s
            """, (
                registro_ativo,
                id_avaliacao
            ))

            alterados = cursor.rowcount

        conexao.commit()

    return alterados > 0


# =========================
# EXCLUIR
# =========================

def excluir(id_avaliacao: int) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                DELETE FROM avaliacoes
                WHERE id = %s
            """, (id_avaliacao,))

            excluidos = cursor.rowcount

        conexao.commit()

    return excluidos > 0