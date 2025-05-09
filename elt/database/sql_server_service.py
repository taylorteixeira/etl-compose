import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv


class SQLServerService:
    def __init__(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
        self.server = os.getenv("SQL_SERVER")
        self.database = os.getenv("SQL_DATABASE")
        self.schema = os.getenv("SQL_SCHEMA")
        self.username = os.getenv("SQL_USERNAME")
        self.password = quote_plus(os.getenv("SQL_PASSWORD"))
        self.engine = self.create_engine()

    def create_engine(self):
        conn_str = f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server"
        return create_engine(conn_str)

    def get_tables(self):
        query = f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = '{self.schema}'"
        return pd.read_sql(query, self.engine)

    def get_table_data(self, table_name):
        query = f"SELECT * FROM {self.schema}.{table_name}"
        return pd.read_sql(query, self.engine)
