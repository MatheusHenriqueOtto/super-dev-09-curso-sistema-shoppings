from typing import Any
from src.database.conexao import conectar
from src.schemas.shoppings import Shopping, ShoppingCadastro, ShoppingEditar


def consultar_todos() -> list[Shopping]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, nome, cnpj, cidade, CAST(registro_ativo AS UNSIGNED)
                FROM shoppings WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Shopping(registro[0], registro[1], registro[2], registro[3], bool(registro[4])) for registro in registros]


def consultar_por_id(id: int) -> Shopping | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nome, cnpj, cidade, CAST(registro_ativo AS UNSIGNED)
                FROM shoppings 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()
            
    if registro is None:
        return None
        
    return Shopping(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        bool(registro[4])
    )


def cadastrar(shopping: ShoppingCadastro) -> Shopping:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO shoppings (nome, cnpj, cidade, registro_ativo) VALUES (%s, %s, %s, 1)", (shopping.nome, shopping.cnpj, shopping.cidade))

            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)

            else:
                raise ValueError("Falha ao obter o ID do shopping cadastrado.")

        conexao.commit()
    return Shopping(novo_id, shopping.nome, shopping.cnpj, shopping.cidade, True)


def atualizar(id: int, shopping: ShoppingEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE shoppings SET nome = %s, cnpj = %s, cidade = %s WHERE id = %s", (shopping.nome, shopping.cnpj, shopping.cidade, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM shoppings WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE shoppings SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM shoppings WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
