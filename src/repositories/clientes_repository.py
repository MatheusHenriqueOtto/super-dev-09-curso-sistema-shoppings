from src.database.conexao import conectar
from src.schemas.clientes import Cliente


def consultar_todos() -> list[Cliente]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nome, cpf, telefone, registro_ativo
                FROM clientes
            """)

            registros = cursor.fetchall()

    clientes = []

    for registro in registros:
        cliente = Cliente(
            id=registro[0],
            nome=registro[1],
            cpf=registro[2],
            telefone=registro[3],
            registro_ativo=registro[4]
        )

        clientes.append(cliente)

    return clientes


def consultar_por_id(id_cliente: int) -> Cliente | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nome, cpf, telefone, registro_ativo
                FROM clientes
                WHERE id = %s
            """, (id_cliente,))

            registro = cursor.fetchone()

    if registro is None:
        return None

    return Cliente(
        id=registro[0],
        nome=registro[1],
        cpf=registro[2],
        telefone=registro[3],
        registro_ativo=registro[4]
    )


def cadastrar(nome: str, cpf: str, telefone: str | None) -> None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                INSERT INTO clientes
                (nome, cpf, telefone, registro_ativo)
                VALUES (%s, %s, %s, 1)
            """, (nome, cpf, telefone))

        conexao.commit()


def atualizar(
    id_cliente: int,
    nome: str,
    cpf: str,
    telefone: str | None
) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE clientes
                SET nome = %s,
                    cpf = %s,
                    telefone = %s
                WHERE id = %s
            """, (nome, cpf, telefone, id_cliente))

            alterados = cursor.rowcount

        conexao.commit()

    return alterados > 0


def alterar_status(id_cliente: int, registro_ativo: bool) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE clientes
                SET registro_ativo = %s
                WHERE id = %s
            """, (registro_ativo, id_cliente))

            alterados = cursor.rowcount

        conexao.commit()

    return alterados > 0


def excluir(id_cliente: int) -> bool:

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                DELETE FROM clientes
                WHERE id = %s
            """, (id_cliente,))

            excluidos = cursor.rowcount

        conexao.commit()

    return excluidos > 0
