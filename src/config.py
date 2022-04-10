from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    MYSQL_HOST = environ.get("MYSQL_HOST")
    MYSQL_PORT = environ.get("MYSQL_PORT")
    MYSQL_USER = environ.get("MYSQL_USER")
    MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
    MYSQL_DATABASE = environ.get("MYSQL_DATABASE")


