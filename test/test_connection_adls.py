from azure.storage.filedatalake import DataLakeServiceClient
import os
from dotenv import load_dotenv
import sys

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=True)

# Recuperar informações da conta e do SAS Token a partir das variáveis de ambiente
account_name = os.getenv("ADLS_ACCOUNT_NAME")
sas_token = os.getenv("ADLS_SAS_TOKEN")

if not account_name or not sas_token:
    print(
        "Erro: Variáveis de ambiente 'ADLS_ACCOUNT_NAME' ou 'ADLS_SAS_TOKEN' não foram definidas."
    )
    sys.exit(1)

# Criar o cliente do Data Lake Service usando o SAS Token
try:
    service_client = DataLakeServiceClient(
        account_url=f"https://{account_name}.dfs.core.windows.net",
        credential=sas_token,
        api_version="2020-02-10",
    )
    # print("Cliente ADLS criado com sucesso usando SAS Token.")
except Exception as e:
    print(f"Erro ao criar o cliente ADLS: {e}")
    sys.exit(1)

# Testar a conexão e listar os file systems
try:
    file_systems = service_client.list_file_systems()
    print("Conexão estabelecida com sucesso. Lista de file systems:")
    for fs in file_systems:
        print(f"- {fs.name}")
except Exception as e:
    print(f"Erro ao listar file systems: {e}")
    sys.exit(1)
