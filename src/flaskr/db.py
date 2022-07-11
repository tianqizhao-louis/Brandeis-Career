from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Table, ForeignKey, Integer, String, UniqueConstraint, Date

 
Base = declarative_base()


class Professor(Base):
    __tablename__ = 'professor'

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Professor({self.professor_id!r}, {self.first_name!r}, {self.last_name!r})"

    def as_dict(self):
        return {
            "professor_id": self.professor_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }


class Gender(Base):
    __tablename__ = 'gender'

    gender_text = Column(String(16), nullable=False, primary_key=True)

    def __init__(self, gender_text):
        self.gender_text = gender_text

    def __repr__(self):
        return f"Gender({self.gender_text!r})"

    def as_dict(self):
        return {
            "gender_text": self.gender_text
        }


class Concentration(Base):
    __tablename__ = 'concentration'

    concentration_id = Column(Integer, primary_key=True, autoincrement=True)
    concentration_name = Column(String(64), nullable=False)
    concentration_type = Column(String(16), nullable=False)

    def __init__(self, concentration_name, concentration_type):
        self.concentration_name = concentration_name
        self.concentration_type = concentration_type

    def __repr__(self):
        return f"Concentration({self.concentration_id!r}, {self.concentration_name!r}, {self.concentration_type!r})"

    def as_dict(self):
        return {
            "concentration_id": self.concentration_id,
            "concentration_name": self.concentration_name,
            "concentration_type": self.concentration_type
        }


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(128), nullable=False)
    company_city = Column(String(64), nullable=True)
    company_state = Column(String(64), nullable=True)

    def __init__(self, company_name, company_city, company_state):
        self.company_name = company_name
        self.company_city = company_city
        self.company_state = company_state

    def __repr__(self):
        return f"Company({self.company_id!r}, {self.company_name!r}, {self.company_city!r}, {self.company_state!r})"

    def as_dict(self):
        return {
            "company_id": self.company_id,
            "company_name": self.company_name,
            "company_city": self.company_city,
            "company_state": self.company_state
        }


class JobMergedTable(Base):
    __tablename__ = 'job_merged_table'

    job_merged_id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(128), nullable=False)

    def __init__(self, job_merged_id, job_name):
        self.job_merged_id = job_merged_id
        self.job_name = job_name

    def __repr__(self):
        return f"JobMergedTable({self.job_merged_id!r}, {self.job_name!r})"

    def as_dict(self):
        return {
            "job_merged_id": self.job_merged_id,
            "job_name": self.job_name
        }


class SocialMedia(Base):
    __tablename__ = 'social_media'

    social_media_id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(32), nullable=False)
    link = Column(String(2083), nullable=False)
    last_updated_date = Column(Date, nullable=False)

    def __init__(self, type, link, last_updated_date):
        self.type = type
        self.link = link
        self.last_updated_date = last_updated_date

    def __repr__(self):
        return f"SocialMedia({self.social_media_id!r}, {self.type!r}, {self.link!r}, {self.last_updated_date!r})"

    def as_dict(self):
        return {
            "social_media_id": self.social_media_id,
            "type": self.type,
            "link": self.link,
            "last_updated_date": self.last_updated_date
        }


class Job(Base):
    __tablename__ = 'job'

    job_id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(128), nullable=False)

    def __init__(self, job_name):
        self.job_name = job_name

    def __repr__(self):
        return f"Job({self.job_id!r}, {self.job_name!r})"

    def as_dict(self):
        return {
            "job_id": self.job_id,
            "job_name": self.job_name
        }


class JobMergeRelationship(Base):
    __tablename__ = 'job_merge_relationship'

    job_id = Column(Integer, ForeignKey('job.job_id'))
    job_merged_id = Column(Integer, ForeignKey('job_merged_table.job_merged_id'))
    # TODO


# from mysql.connector import connect, Error
# from datetime import datetime, date

#
# class Database:
#     def __init__(self, host, port, user, password, database):
#         self.host = host
#         self.port = port
#         self.user = user
#         self.password = password
#         self.database = database
#
#         try:
#             with connect(
#                     host=self.host,
#                     port=self.port,
#                     user=self.user,
#                     password=self.password,
#                     database=self.database
#             ) as connection:
#                 print('Database Connected')
#         except Error as e:
#             print(e)
#
#     def get_connection(self):
#         db_connection = connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )
#         return db_connection
#
#     @staticmethod
#     def close_connection(db_connection):
#         db_connection.close()
#
#     def get_professor_table_all(self):
#         professor_table_schema = ProfessorSchema(self.get_connection())
#         return_table = professor_table_schema.select_all(self.get_connection())
#         return professor_table_schema.schema_name, professor_table_schema.column_names, return_table
#
#     def get_gender_table_all(self):
#         gender_table_schema = GenderSchema(self.get_connection())
#         return_table = gender_table_schema.select_all(self.get_connection())
#         return gender_table_schema.schema_name, gender_table_schema.column_names, return_table
#
#     def get_concentration_table_all(self):
#         concentration_table_schema = ConcentrationSchema(self.get_connection())
#         return_table = concentration_table_schema.select_all(self.get_connection())
#         return concentration_table_schema.schema_name, concentration_table_schema.column_names, return_table
#
#     def get_job_merged_table_all(self):
#         job_merged_table_schema = JobMergedTableSchema(self.get_connection())
#         return_table = job_merged_table_schema.select_all(self.get_connection())
#         return job_merged_table_schema.schema_name, job_merged_table_schema.column_names, return_table
#
#     def get_company_table_all(self):
#         company_schema = CompanySchema(self.get_connection())
#         return_table = company_schema.select_all(self.get_connection())
#         return company_schema.schema_name, company_schema.column_names, return_table
#
#     def get_alumni_table_all(self):
#         alumni_schema = AlumniSchema(self.get_connection())
#         return_table = alumni_schema.select_all(self.get_connection())
#         return alumni_schema.schema_name, alumni_schema.column_names, return_table
#
#     def insert_into_professor_table(self, data):
#         professor_schema = ProfessorSchema(self.get_connection())
#         inserted_id = professor_schema.insert_new(db_connection=self.get_connection(),
#                                                   data=data)
#         return inserted_id
#
#     def get_schema_column_names(self, schema_name):
#         if schema_name == 'professor':
#             professor_schema = ProfessorSchema(self.get_connection())
#             return professor_schema.return_insertable_columns()
#
#
# class Schema:
#     def __init__(self, db_connection, schema_name):
#         describe_clause = """DESCRIBE """ + schema_name
#         with db_connection.cursor() as cursor:
#             cursor.execute(describe_clause)
#             column_tuple = cursor.fetchall()
#
#         # column names of the table
#         self.column_names = []
#         for each_column_tuple in column_tuple:
#             self.column_names.append(each_column_tuple[0])
#
#         # schema name
#         self.schema_name = schema_name
#
#         self.column_data_type = []
#         data_type_clause = """SELECT DATA_TYPE
#                               FROM INFORMATION_SCHEMA.COLUMNS
#                               WHERE table_name = '%s'
#                            """ % self.schema_name
#         with db_connection.cursor() as cursor:
#             cursor.execute(data_type_clause)
#             data_type = cursor.fetchall()
#         for each_data_type in data_type:
#             first_item = each_data_type[0]
#             if first_item == 'int' or first_item == 'year':
#                 self.column_data_type.append("int")
#             elif first_item == 'varchar':
#                 self.column_data_type.append("str")
#             else:
#                 self.column_data_type.append(first_item)
#
#         self.close_connection(db_connection)
#
#     def select_all(self, db_connection):
#         sql_line = self.make_sql_select_all()
#         with db_connection.cursor() as cursor:
#             cursor.execute(sql_line)
#             tb = cursor.fetchall()
#         self.close_connection(db_connection)
#         return self.format_dict_table(tb)
#
#     def format_dict_table(self, alumni_table):
#         format_dict = {}
#         for row in alumni_table:
#             each_column_dict = {}
#             for index in range(len(self.column_names)):
#                 if isinstance(row[index], date):
#                     # convert a datetime.date class to string format of yyyy/mm/dd
#                     each_column_dict[self.column_names[index]] = row[index].strftime('%Y/%m/%d')
#                 else:
#                     # other cases
#                     each_column_dict[self.column_names[index]] = row[index]
#             format_dict[each_column_dict[self.column_names[0]]] = each_column_dict
#         return format_dict
#
#     def make_sql_select_all(self):
#         select_clause = """SELECT """
#
#         select_from_table_name = []
#         for column in self.column_names:
#             select_from_table_name.append(column + ' AS \'' + column + '\'')
#         stringify_append_table_name = ", ".join(select_from_table_name)
#
#         from_clause = [" ", "FROM ", self.schema_name]
#         stringify_from_clause = "".join(from_clause)
#         return "".join((select_clause, stringify_append_table_name, stringify_from_clause))
#
#     @staticmethod
#     def close_connection(db_connection):
#         db_connection.close()
#
#     @staticmethod
#     def commit_connection(db_connection):
#         db_connection.commit()
#
#     def make_sql_insert_new(self):
#         insert_clause = """INSERT INTO """ + self.schema_name
#         insertable_columns = []
#         for index in range(len(self.column_names)):
#             if index == 0:
#                 continue
#             else:
#                 insertable_columns.append(self.column_names[index])
#         insertable_columns_string = ", ".join(insertable_columns)
#         full_column_names = "".join((" (", insertable_columns_string, ")"))
#
#         values_clause = """ VALUES """
#
#         final_clause = "".join((insert_clause, full_column_names, values_clause))
#         return final_clause
#
#     def make_sql_insert_new_with_data(self, data):
#         final_clause_with_data = []
#
#         no_data_clause = self.make_sql_insert_new()
#
#         data_list = []
#         for index in range(len(data)):
#             if self.column_data_type[index + 1] == 'str':
#                 data_list.append("'{" + str(index) + "}'")
#             elif self.column_data_type[index + 1] == 'int':
#                 data_list.append("{" + str(index) + "}")
#             else:
#                 data_list.append("'{" + str(index) + "}'")
#
#         str_data_list = ", ".join(data_list)
#         temp_clause = "(" + str_data_list.format(*data) + ")"
#
#         final_clause_with_data.append(no_data_clause)
#         final_clause_with_data.append(temp_clause)
#
#         return "".join(final_clause_with_data)
#
#     def insert_new(self, db_connection, data):
#         sql_line = self.make_sql_insert_new_with_data(data=data)
#         with db_connection.cursor() as cursor:
#             cursor.execute(sql_line)
#             self.commit_connection(db_connection)
#         return_id = self.get_newest_insert_id(db_connection=db_connection)
#         print(return_id)
#         self.close_connection(db_connection)
#         return return_id
#
#     def get_newest_insert_id(self, db_connection):
#         sql_line = ["SELECT", self.column_names[0], "FROM", self.schema_name, "ORDER BY", self.column_names[0],
#                     "DESC LIMIT 1"]
#         str_sql = " ".join(sql_line)
#         with db_connection.cursor() as cursor:
#             cursor.execute(str_sql)
#             return_id = cursor.fetchone()
#         return return_id[0]
#
#     def return_insertable_columns(self):
#         return self.column_names[1:]
#
#
# class AlumniSchema(Schema):
#     def __init__(self, db_connection, schema_name="alumni"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
#
#
# class ProfessorSchema(Schema):
#     def __init__(self, db_connection, schema_name="professor"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
#
#
# class GenderSchema(Schema):
#     def __init__(self, db_connection, schema_name="gender"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
#
#
# class ConcentrationSchema(Schema):
#     def __init__(self, db_connection, schema_name="concentration"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
#
#
# class JobMergedTableSchema(Schema):
#     def __init__(self, db_connection, schema_name="job_merged_table"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
#
#
# class CompanySchema(Schema):
#     def __init__(self, db_connection, schema_name="company"):
#         super().__init__(db_connection=db_connection, schema_name=schema_name)
