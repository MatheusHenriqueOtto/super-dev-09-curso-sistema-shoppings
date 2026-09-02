from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from src.settings.settings import configuracoes


def conectar() -> PooledMySQLConnection | MySQLConnectionAbstract:
    """Abre uma conexão; o chamador é responsável por fechá-la."""
    return connect(
        host=configuracoes.db_host,
        port=configuracoes.db_port,
        user=configuracoes.db_user,
        password=configuracoes.db_pass,
        database=configuracoes.db_name,
    )

