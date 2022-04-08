from mysql.connector import connect, Error


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
                print('Database connected')
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

    def get_basic_view(self):
        db_connection = self.get_connection()
        sql_line = """SELECT alumni.alumni_id AS 'alumni_id',
            alumni.first_name AS 'first_name',
            alumni.last_name AS 'last_name',
            gender.gender_text AS 'gender',
            alumni.class_year AS 'class_year',
            alumni.email AS 'email',
            alumni.current_location_city AS 'city',
            alumni.current_location_state AS 'state',
            alumni.alumni_type AS 'alumni_type',
            alumni.last_updated_date AS 'last_updated_by'
            FROM alumni
            INNER JOIN gender ON alumni.gender = gender.gender_text;"""
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
            for row in result:
                print(row)
            # db_connection.commit()
        self.close_connection(db_connection)

    def get_professor_table_all(self):
        db_connection = self.get_connection()
        sql_line = """
            SELECT professor.professor_id AS 'professor_id',
                professor.first_name AS 'first_name',
                professor.last_name AS 'last_name'
            FROM professor                
        """
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        table_dict = {}

        for each_prof in result:
            professor_id = int(each_prof[0])
            first_name = str(each_prof[1])
            last_name = str(each_prof[2])
            new_prof = Professor(professor_id=professor_id,
                                 first_name=first_name,
                                 last_name=last_name)
            table_dict[professor_id] = vars(new_prof)
        professor_table = ProfessorTable(table_dict=table_dict)
        return vars(professor_table)

    def get_gender_table_all(self):
        db_connection = self.get_connection()
        sql_line = """SELECT gender.gender_text AS 'gender' FROM gender"""
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        table_dict = {}

        for each_gender in result:
            gender_text = str(each_gender[0])
            new_gender = Gender(gender_text=gender_text)
            table_dict[gender_text] = vars(new_gender)
        gender_table = GenderTable(table_dict=table_dict)
        return vars(gender_table)

    def get_concentration_table_all(self):
        db_connection = self.get_connection()
        sql_line = """
            SELECT concentration_id AS 'concentration_id',
                concentration_name AS 'concentration_name',
                concentration_type AS 'concentration_type'
            FROM concentration
        """
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        table_dict = {}

        for each_concentration in result:
            concentration_id = int(each_concentration[0])
            concentration_name = str(each_concentration[1])
            concentration_type = str(each_concentration[2])
            new_concentration = Concentration(concentration_id=concentration_id,
                                              concentration_name=concentration_name,
                                              concentration_type=concentration_type)
            table_dict[concentration_id] = vars(new_concentration)
        concentration_table = ConcentrationTable(table_dict=table_dict)
        return vars(concentration_table)

    def get_job_merged_table_all(self):
        db_connection = self.get_connection()
        sql_line = """
            SELECT job_merged_id AS 'job_merged_id',
                job_name AS 'job_name'
            FROM job_merged_table
        """
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        table_dict = {}

        for each_job_merged in result:
            job_merged_id = int(each_job_merged[0])
            job_name = str(each_job_merged[1])
            new_each_job_merged = JobMerged(job_merged_id=job_merged_id,
                                            job_name=job_name)
            table_dict[job_merged_id] = vars(new_each_job_merged)
        job_merged_table_collect = JobMergedTable(table_dict=table_dict)
        return vars(job_merged_table_collect)

    def get_company_table_all(self):
        db_connection = self.get_connection()
        sql_line = """
            SELECT company_id AS 'company_id',
                company_name AS 'company_name',
                company_city AS 'company_city',
                company_state AS 'company_state'
            FROM company
        """
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        table_dict = {}

        for each_company in result:
            company_id = int(each_company[0])
            company_name = str(each_company[1])
            company_city = str(each_company[2])
            company_state = str(each_company[3])
            new_company = Company(company_id=company_id,
                                  company_name=company_name,
                                  company_city=company_city,
                                  company_state=company_state)
            table_dict[company_id] = vars(new_company)
        company_table = CompanyTable(table_dict=table_dict)
        return vars(company_table)


class Alumni:
    def __init__(self, alumni_id, referred_prof_id, gender, social_media_id,
                 first_name, last_name, class_year, email, current_location_city,
                 current_location_state, alumni_type, last_updated_date):
        self.alumni_id = alumni_id
        self.referred_prof_id = referred_prof_id
        self.gender = gender
        self.social_media_id = social_media_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_year = class_year
        self.email = email
        self.current_location_city = current_location_city
        self.current_location_state = current_location_state
        self.alumni_type = alumni_type
        self.last_updated_date = last_updated_date


class Professor:
    def __init__(self, professor_id, first_name, last_name):
        self.professor_id = professor_id
        self.first_name = first_name
        self.last_name = last_name


class ProfessorTable:
    def __init__(self, table_dict, schema=None, table_name="professor"):
        if schema is None:
            schema = ["professor_id", "first_name", "last_name"]
        self.table_name = table_name
        self.schema = schema

        self.table_dict = table_dict


class Gender:
    def __init__(self, gender_text):
        self.gender_text = gender_text


class GenderTable:
    def __init__(self, table_dict, schema=None, table_name="gender"):
        if schema is None:
            schema = ["gender_text"]
        self.table_name = table_name
        self.schema = schema

        self.table_dict = table_dict


class Concentration:
    def __init__(self, concentration_id, concentration_name, concentration_type):
        self.concentration_id = concentration_id
        self.concentration_name = concentration_name
        self.concentration_type = concentration_type


class ConcentrationTable:
    def __init__(self, table_dict, schema=None, table_name="concentration"):
        if schema is None:
            schema = ["concentration_id", "concentration_name", "concentration_type"]
        self.schema = schema
        self.table_name = table_name

        self.table_dict = table_dict


class JobMerged:
    def __init__(self, job_merged_id, job_name):
        self.job_merged_id = job_merged_id
        self.job_name = job_name


class JobMergedTable:
    def __init__(self, table_dict, schema=None, table_name="job_merged_table"):
        if schema is None:
            schema = ["job_merged_id", "job_name"]
        self.schema = schema
        self.table_name = table_name

        self.table_dict = table_dict


class Company:
    def __init__(self, company_id, company_name, company_city, company_state):
        self.company_id = company_id
        self.company_name = company_name
        self.company_city = company_city
        self.company_state = company_state


class CompanyTable:
    def __init__(self, table_dict, schema=None, table_name="company"):
        if schema is None:
            schema = ["company_id", "company_name", "company_city", "company_state"]
        self.schema = schema
        self.table_name = table_name

        self.table_dict = table_dict
