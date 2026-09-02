import sys
from pathlib import Path
from typing import Any

# Garante que o Python consiga encontrar a pasta 'src'
sys.path.append(str(Path(__file__).resolve().parent))

try:
    # Tenta importar sua função de conexão e suas configurações
    from src.database.conexao import conectar
    from src.settings.settings import configuracoes
    
    print("🔄 Tentando conectar ao banco de dados...")
    print(f"📍 Host: {configuracoes.db_host}")
    print(f"📦 Banco: {configuracoes.db_name}")
    print(f"🔌 Porta: {configuracoes.db_port}")
    print(f"👤 Usuário: {configuracoes.db_user}")
    print("-" * 40)

    # Executa a conexão exatamente como seu repositório faz
    with conectar() as conexao:
        if conexao.is_connected():
            print("✅ SUCESSO: Conexão com o MySQL estabelecida com êxito!")
            
            # Testa uma consulta simples para garantir que o banco responde
            with conexao.cursor() as cursor:
                cursor.execute("SELECT VERSION();")
                versao: Any = cursor.fetchone()
                print(f"🤖 Versão do MySQL: {versao[0]}")

except Exception as erro:
    print("\n❌ ERRO: Falha ao conectar ao banco de dados!")
    print(f"📁 Detalhes do erro: {erro}")
