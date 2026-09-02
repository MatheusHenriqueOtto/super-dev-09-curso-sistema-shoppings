from typing import Any
from src.database.conexao import conectar
from src.schemas.lojas import Loja, LojaCadastro, LojaEditar


def consultar_todos() -> list[Loja]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, nome_fantasia, numero_modulo, id_shopping, CAST(registro_ativo AS UNSIGNED)
                FROM lojas WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Loja(registro[0], registro[1], registro[2], registro[3], bool(registro[4])) for registro in registros]


def consultar_por_id(id: int) -> Loja | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, nome_fantasia, numero_modulo, id_shopping, CAST(registro_ativo AS UNSIGNED)
                FROM lojas 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()
            
    if registro is None:
        return None
        
    return Loja(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        bool(registro[4])
    )



def cadastrar(loja: LojaCadastro) -> Loja:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO lojas (nome_fantasia, numero_modulo, id_shopping, registro_ativo) VALUES (%s, %s, %s, 1)", (loja.nome_fantasia, loja.numero_modulo, loja.id_shopping))

            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)

            else:
                raise ValueError("Falha ao obter o ID da loja cadastrada.")        

        conexao.commit()

    return Loja(novo_id, loja.nome_fantasia, loja.numero_modulo, loja.id_shopping, True)


def atualizar(id: int, loja: LojaEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE lojas SET nome_fantasia = %s, numero_modulo = %s, id_shopping = %s WHERE id = %s", (loja.nome_fantasia, loja.numero_modulo, loja.id_shopping, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM lojas WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE lojas SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM lojas WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
