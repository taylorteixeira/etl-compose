import os
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import ResourceExistsError
from dotenv import load_dotenv


class ADLSService:
    def __init__(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
        self.account_name = os.getenv("ADLS_ACCOUNT_NAME")
        self.file_system_name = os.getenv("ADLS_FILE_SYSTEM_NAME")
        self.directory_name = os.getenv("ADLS_DIRECTORY_NAME")
        self.sas_token = os.getenv("ADLS_SAS_TOKEN")
        self.client = DataLakeServiceClient(
            account_url=f"https://{self.account_name}.dfs.core.windows.net",
            credential=self.sas_token,
            api_version="2020-02-10",
        )
        self.directory_client = self.get_directory_client()

    def get_directory_client(self):
        file_system_client = self.client.get_file_system_client(self.file_system_name)
        directory_client = file_system_client.get_directory_client(self.directory_name)
        try:
            directory_client.create_directory()
        except ResourceExistsError:
            print(f"O diretório '{self.directory_name}' já existe.")
        return directory_client

    def upload_data(self, file_name, data):
        file_client = self.directory_client.get_file_client(file_name)
        file_client.upload_data(data, overwrite=True)
        print(f"Arquivo '{file_name}' carregado com sucesso no ADLS.")
