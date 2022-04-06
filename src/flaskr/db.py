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

        result_dict = {}

        for each_prof in result:
            professor_id = int(each_prof[0])
            first_name = str(each_prof[1])
            last_name = str(each_prof[2])
            new_prof = Professor(professor_id=professor_id,
                                 first_name=first_name,
                                 last_name=last_name)
            result_dict[professor_id] = vars(new_prof)
        return result_dict

    def get_gender_table_all(self):
        db_connection = self.get_connection()
        sql_line = """SELECT gender.gender_text AS 'gender' FROM gender"""
        with db_connection.cursor() as cursor:
            cursor.execute(sql_line)
            result = cursor.fetchall()
        self.close_connection(db_connection)

        result_list = []

        for each_gender in result:
            gender_text = str(each_gender[0])
            new_gender = Gender(gender_text=gender_text)
            result_list.append(vars(new_gender))
        return result_list


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


class Gender:
    def __init__(self, gender_text):
        self.gender_text = gender_text
