from typing import Any
from src.database.conexao import conectar
from src.schemas.funcionarios import Funcionario, FuncionarioCadastro, FuncionarioEditar


def consultar_todos() -> list[Funcionario]:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT id, id_loja, nome, cpf, cargo, CAST(registro_ativo AS UNSIGNED)
                FROM funcionarios WHERE registro_ativo = b'1'""")
            registros: list = cursor.fetchall()
    return [Funcionario(registro[0], registro[1], registro[2], registro[3], registro[4], bool(registro[5])) for registro in registros]


def consultar_por_id(id: int) -> Funcionario | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, id_loja, nome, cpf, cargo, CAST(registro_ativo AS UNSIGNED)
                FROM funcionarios 
                WHERE id = %s AND registro_ativo = b'1'
            """, (id,))
            registro: Any = cursor.fetchone()
            
    if registro is None:
        return None
        
    return Funcionario(
        registro[0],
        registro[1],
        registro[2],
        registro[3],
        registro[4],
        bool(registro[5])
    )


def cadastrar(funcionario: FuncionarioCadastro) -> Funcionario:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO funcionarios (id_loja, nome, cpf, cargo, registro_ativo) VALUES (%s, %s, %s, %s, 1)", (funcionario.id_loja, funcionario.nome, funcionario.cpf, funcionario.cargo))

            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)

            else:
                raise ValueError("Falha ao obter o ID do funcionario cadastrado.")        

    conexao.commit()

    return Funcionario(novo_id, funcionario.id_loja, funcionario.nome, funcionario.cpf, funcionario.cargo, True)


def atualizar(id: int, funcionario: FuncionarioEditar) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE funcionarios SET id_loja = %s, nome = %s, cpf = %s, cargo = %s WHERE id = %s", (funcionario.id_loja, funcionario.nome, funcionario.cpf, funcionario.cargo, id))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado


def alterar_status(id: int, registro_ativo: bool) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id FROM funcionarios WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("UPDATE funcionarios SET registro_ativo = %s WHERE id = %s", (registro_ativo, id))
        conexao.commit()
    return True


def excluir(id: int) -> bool:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id,))
            resultado = cursor.rowcount > 0
        conexao.commit()
    return resultado
