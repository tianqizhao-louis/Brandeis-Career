from src.flaskr.db import CompanySchema
from src.flaskr.db import Database
from dotenv import load_dotenv
import os

load_dotenv()
database_server = Database(host=os.environ.get("MYSQL_HOST"),
                           user=os.environ.get("MYSQL_USER"),
                           password=os.environ.get("MYSQL_PASSWORD"),
                           database=os.environ.get("MYSQL_DATABASE"))

print(database_server.get_professor_table_all())
