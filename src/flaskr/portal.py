import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from .db import Database
from dotenv import load_dotenv

bp = Blueprint('portal', __name__)


@bp.route('/admin', methods=['GET'])
def admin():
    return render_template("admin/admin_home.html")


@bp.route('/admin/table/<string:table_type>', methods=['GET'])
def render_table(table_type):
    load_dotenv()
    database_server = Database(host=os.environ.get("MYSQL_HOST"),
                      user=os.environ.get("MYSQL_USER"),
                      password=os.environ.get("MYSQL_PASSWORD"),
                      database=os.environ.get("MYSQL_DATABASE"))

    data_tuple = None
    if table_type == 'professor':
        data_tuple = database_server.get_professor_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
    elif table_type == 'gender':
        data_tuple = database_server.get_gender_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
    elif table_type == 'concentration':
        data_tuple = database_server.get_concentration_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
    elif table_type == 'job-merged-table':
        data_tuple = database_server.get_job_merged_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
    elif table_type == 'company':
        data_tuple = database_server.get_company_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
    elif table_type == 'alumni':
        data_tuple = database_server.get_alumni_table_all()
        return render_template("admin/table_render.html",
                               table_type=data_tuple[0],
                               table_columns=data_tuple[1],
                               table_dict=data_tuple[2])
