from mysql.connector import connect, Error
from datetime import datetime, date


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connection:
                print('Database Connected')
        except Error as e:
            print(e)

    def get_connection(self):
        db_connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return db_connection

    @staticmethod
    def close_connection(db_connection):
        db_connection.close()

    def get_professor_table_all(self):
        professor_table_schema = ProfessorSchema(self.get_connection())
        return_table = professor_table_schema.select_all(self.get_connection())
        return professor_table_schema.schema_name, professor_table_schema.column_names, return_table

    def get_gender_table_all(self):
        gender_table_schema = GenderSchema(self.get_connection())
        return_table = gender_table_schema.select_all(self.get_connection())
        return gender_table_schema.schema_name, gender_table_schema.column_names, return_table

    def get_concentration_table_all(self):
        concentration_table_schema = ConcentrationSchema(self.get_connection())
        return_table = concentration_table_schema.select_all(self.get_connection())
        return concentration_table_schema.schema_name, concentration_table_schema.column_names, return_table

    def get_job_merged_table_all(self):
        job_merged_table_schema = JobMergedTableSchema(self.get_connection())
        return_table = job_merged_table_schema.select_all(self.get_connection())
        return job_merged_table_schema.schema_name, job_merged_table_schema.column_names, return_table

    def get_company_table_all(self):
        company_schema = CompanySchema(self.get_connection())
        return_table = company_schema.select_all(self.get_connection())
        return company_schema.schema_name, company_schema.column_names, return_table

    def get_alumni_table_all(self):
        alumni_schema = AlumniSchema(self.get_connection())
        return_table = alumni_schema.select_all(self.get_connection())
        return alumni_schema.schema_name, alumni_schema.column_names, return_table


class Schema:
    def __init__(self, db_connection, schema_name):
        sql_line = """DESCRIBE """ + schema_name
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            column_tuple = cursor.fetchall()
        self.close_connection(db_connection)

        # column names of the table
        self.column_names = []
        for each_column_tuple in column_tuple:
            self.column_names.append(each_column_tuple[0])

        # schema name
        self.schema_name = schema_name

    def select_all(self, db_connection):
        sql_line = self.make_sql_select_all()
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            tb = cursor.fetchall()
        self.close_connection(db_connection)
        return self.format_dict_table(tb)

    def format_dict_table(self, alumni_table):
        format_dict = {}
        for row in alumni_table:
            each_column_dict = {}
            for index in range(len(self.column_names)):
                if isinstance(row[index], date):
                    # convert a datetime.date class to string format of yyyy/mm/dd
                    each_column_dict[self.column_names[index]] = row[index].strftime('%Y/%m/%d')
                else:
                    # other cases
                    each_column_dict[self.column_names[index]] = row[index]
            format_dict[each_column_dict[self.column_names[0]]] = each_column_dict
        return format_dict

    def make_sql_select_all(self):
        select_clause = """SELECT """

        select_from_table_name = []
        for column in self.column_names:
            select_from_table_name.append(column + ' AS \'' + column + '\'')
        stringify_append_table_name = ", ".join(select_from_table_name)

        from_clause = [" ", "FROM ", self.schema_name]
        stringify_from_clause = "".join(from_clause)
        return "".join((select_clause, stringify_append_table_name, stringify_from_clause))

    @staticmethod
    def close_connection(db_connection):
        db_connection.close()


class AlumniSchema(Schema):
    def __init__(self, db_connection, schema_name="alumni"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)


class ProfessorSchema(Schema):
    def __init__(self, db_connection, schema_name="professor"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)


class GenderSchema(Schema):
    def __init__(self, db_connection, schema_name="gender"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)


class ConcentrationSchema(Schema):
    def __init__(self, db_connection, schema_name="concentration"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)


class JobMergedTableSchema(Schema):
    def __init__(self, db_connection, schema_name="job_merged_table"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)


class CompanySchema(Schema):
    def __init__(self, db_connection, schema_name="company"):
        super().__init__(db_connection=db_connection, schema_name=schema_name)
