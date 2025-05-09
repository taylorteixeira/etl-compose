import os
from sqlalchemy import create_engine, text  # Importar text do SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=True)

# Configurações do SQL Server
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = quote_plus(os.getenv("SQL_PASSWORD"))

# Criar a string de conexão
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Criar engine do SQLAlchemy
engine = create_engine(conn_str)

try:
    # Testar a conexão
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT 1")
        )  # Usar text para executar a consulta
        print("Conexão estabelecida com sucesso.")
except Exception as e:
    print(f"Erro ao conectar: {e}")
