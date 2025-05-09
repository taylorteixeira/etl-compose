from azure_integration.adls_service import ADLSService
from database.sql_server_service import SQLServerService


def upload_sqlserver_to_adls():
    sql_service = SQLServerService()
    adls_service = ADLSService()

    tables_df = sql_service.get_tables()
    for _, row in tables_df.iterrows():
        table_name = row["table_name"]
        df = sql_service.get_table_data(table_name)
        csv_data = df.to_csv(index=False).encode()
        adls_service.upload_data(f"{table_name}.csv", csv_data)


if __name__ == "__main__":
    # Escolha o banco de dados: SQL Server ou MongoDB
    upload_sqlserver_to_adls()
