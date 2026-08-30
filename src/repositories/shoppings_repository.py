from src.database.conexao import conectar
from src.schemas.shoppings import Shopping

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

