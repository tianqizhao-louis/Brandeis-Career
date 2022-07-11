# import sqlalchemy as db
# import os
# load_dotenv()
#
# host=os.environ.get("MYSQL_HOST")
# port=str(os.environ.get("MYSQL_PORT"))
# user=os.environ.get("MYSQL_USER")
# password=os.environ.get("MYSQL_PASSWORD")
# database=os.environ.get("MYSQL_DATABASE")
#
# engine = db.create_engine('mysql+mysqlconnector://root:dbrootdbroot@localhost:3306/dareer')
# connection = engine.connect()
# metadata = db.MetaData()
#
# professor = db.Table('professor', metadata, autoload=True, autoload_with=engine)
#
# query = db.select([professor])
#
# ResultProxy = connection.execute(query)
#
# ResultSet = ResultProxy.fetchall()
#
# print(ResultSet)
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from flask import current_app

from src.flaskr.db import Professor, Gender, Concentration

import os


class Database:
    def __init__(self):
        # host = current_app.config["MYSQL_HOST"]
        # port = current_app.config["MYSQL_PORT"]
        # user = current_app.config["MYSQL_USER"]
        # password = current_app.config["MYSQL_PASSWORD"]
        # database = current_app.config["MYSQL_DATABASE"]

        load_dotenv()
        host = os.environ.get("MYSQL_HOST")
        port = os.environ.get("MYSQL_PORT")
        user = os.environ.get("MYSQL_USER")
        password = os.environ.get("MYSQL_PASSWORD")
        database = os.environ.get("MYSQL_DATABASE")

        engine_server = """mysql+mysqlconnector://%s:%s@%s:%s/%s""" % (user, password, host, port, database)
        self.engine = create_engine(engine_server)
        self.metadata = MetaData()

    def select(self):
        from sqlalchemy.orm import load_only

        with Session(self.engine) as session:
            stmt = select(Gender)
            p = session.query(Gender).all()
            for a in p:
                print(a.as_dict())

    def insert(self):
        with Session(self.engine) as session:
            # prof = Professor(first_name=first_name, last_name=last_name)
            # session.add(prof)
            # session.commit()
            gd = Concentration(concentration_name="Math", concentration_type="minor")
            session.add(gd)
            session.commit()



db = Database()
# db.insert(first_name='test_orm', last_name='finish_test_orm')

db.insert()