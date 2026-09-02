from src.database.conexao import conectar
from src.schemas.shoppings import Shopping, ShoppingCadastro, ShoppingEditar

def consultar_todos() -> list[Shopping] | None:
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            sql = """SELECT 
                id, 
                nome, 
                cnpj, 
                cidade, 
                CAST(registro_ativo AS UNSIGNED) AS registro_ativo
            FROM shoppings
            WHERE registro_ativo = b'1';"""
            cursor.execute(sql)
            registros: list = cursor.fetchall()


    shoppings: list[Shopping] = []
    for registro in registros:
        shopping = Shopping(
            id=registro[0], 
            nome=registro[1], 
            cnpj=registro[2], 
            cidade=registro[3], 
            registro_ativo=registro[4])
        shoppings.append(shopping)

    return shoppings


def cadastrar(shopping: ShoppingCadastro) -> Shopping:
    """Responsavel por cadstrar um shopping a tabela de shopings"""
    sql = """INSERT INTO shoppings (nome, cnpj, cidade) VALUES (%s, %s, %s)"""
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (
                shopping.nome,
                shopping.cnpj,
                shopping.cidade
            ))

            conexao.commit()

            if cursor.lastrowid is not None:
                novo_id: int = int(cursor.lastrowid)
            else:
                raise ValueError("Falha ao obter o ID do shopping cadastrado.")

    return Shopping(
        id=novo_id,
        nome=shopping.nome,
        cnpj=shopping.cnpj,
        cidade=shopping.cidade,
        registro_ativo=True
    )


def editar(id: int, shopping: ShoppingEditar):
    sql = """UPDATE shoppings SET
        nome=%s,
        cnpj=%s,
        cidade=%s
    WHERE id=%s
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (
                shopping.nome,
                shopping.cnpj,
                shopping.cidade,
                id
            ))
            conexao.commit()


def consultar_por_id(id: int):
    pass