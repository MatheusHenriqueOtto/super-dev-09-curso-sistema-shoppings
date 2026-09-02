from typing import Any
from src.database.conexao import conectar
from src.schemas.clientes import Cliente, ClienteCadastro, ClienteEditar


def consultar_todos() -> list[Cliente]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, nome, cpf, telefone, CAST(registro_ativo AS UNSIGNED)
                FROM clientes WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Cliente(registro[0], registro[1], registro[2], registro[3], bool(registro[4])) for registro in registros]


def consultar_por_id(id: int) -> Cliente | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nome, cpf, telefone, CAST(registro_ativo AS UNSIGNED)
                FROM clientes 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()

    if registro is None:
        return None

    return Cliente(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        bool(registro[4])
    )


def cadastrar(cliente: ClienteCadastro) -> Cliente:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO clientes (nome, cpf, telefone, registro_ativo) VALUES (%s, %s, %s, 1)", (cliente.nome, cliente.cpf, cliente.telefone))
            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)
            
            else:
                raise ValueError("Falha ao obter o ID do cliente cadastrado.")
            
        conexao.commit()
    return Cliente(novo_id, cliente.nome, cliente.cpf, cliente.telefone, True)


def atualizar(id: int, cliente: ClienteEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE clientes SET nome = %s, cpf = %s, telefone = %s WHERE id = %s", (cliente.nome, cliente.cpf, cliente.telefone, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM clientes WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE clientes SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
