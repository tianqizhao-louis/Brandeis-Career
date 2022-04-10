from mysql.connector import connect, Error
from datetime import datetime, date


class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        try:
            with connect(
                    host=self.host,
                    port=self.port,
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

    def insert_into_professor_table(self, data):
        professor_schema = ProfessorSchema(self.get_connection())
        inserted_id = professor_schema.insert_new(db_connection=self.get_connection(),
                                                  data=data)
        return inserted_id

    def get_schema_column_names(self, schema_name):
        if schema_name == 'professor':
            professor_schema = ProfessorSchema(self.get_connection())
            return professor_schema.return_insertable_columns()


class Schema:
    def __init__(self, db_connection, schema_name):
        describe_clause = """DESCRIBE """ + schema_name
        with db_connection.cursor() as cursor:
            cursor.execute(describe_clause)
            column_tuple = cursor.fetchall()

        # column names of the table
        self.column_names = []
        for each_column_tuple in column_tuple:
            self.column_names.append(each_column_tuple[0])

        # schema name
        self.schema_name = schema_name

        self.column_data_type = []
        data_type_clause = """SELECT DATA_TYPE 
                              FROM INFORMATION_SCHEMA.COLUMNS 
                              WHERE table_name = '%s'
                           """ % self.schema_name
        with db_connection.cursor() as cursor:
            cursor.execute(data_type_clause)
            data_type = cursor.fetchall()
        for each_data_type in data_type:
            first_item = each_data_type[0]
            if first_item == 'int' or first_item == 'year':
                self.column_data_type.append("int")
            elif first_item == 'varchar':
                self.column_data_type.append("str")
            else:
                self.column_data_type.append(first_item)

        self.close_connection(db_connection)

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

    @staticmethod
    def commit_connection(db_connection):
        db_connection.commit()

    def make_sql_insert_new(self):
        insert_clause = """INSERT INTO """ + self.schema_name
        insertable_columns = []
        for index in range(len(self.column_names)):
            if index == 0:
                continue
            else:
                insertable_columns.append(self.column_names[index])
        insertable_columns_string = ", ".join(insertable_columns)
        full_column_names = "".join((" (", insertable_columns_string, ")"))

        values_clause = """ VALUES """

        final_clause = "".join((insert_clause, full_column_names, values_clause))
        return final_clause

    def make_sql_insert_new_with_data(self, data):
        final_clause_with_data = []

        no_data_clause = self.make_sql_insert_new()

        data_list = []
        for index in range(len(data)):
            if self.column_data_type[index + 1] == 'str':
                data_list.append("'{" + str(index) + "}'")
            elif self.column_data_type[index + 1] == 'int':
                data_list.append("{" + str(index) + "}")
            else:
                data_list.append("'{" + str(index) + "}'")

        str_data_list = ", ".join(data_list)
        temp_clause = "(" + str_data_list.format(*data) + ")"

        final_clause_with_data.append(no_data_clause)
        final_clause_with_data.append(temp_clause)

        return "".join(final_clause_with_data)

    def insert_new(self, db_connection, data):
        sql_line = self.make_sql_insert_new_with_data(data=data)
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            self.commit_connection(db_connection)
        return_id = self.get_newest_insert_id(db_connection=db_connection)
        print(return_id)
        self.close_connection(db_connection)
        return return_id

    def get_newest_insert_id(self, db_connection):
        sql_line = ["SELECT", self.column_names[0], "FROM", self.schema_name, "ORDER BY", self.column_names[0],
                    "DESC LIMIT 1"]
        str_sql = " ".join(sql_line)
        with db_connection.cursor() as cursor:
            cursor.execute(str_sql)
            return_id = cursor.fetchone()
        return return_id[0]

    def return_insertable_columns(self):
        return self.column_names[1:]


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
