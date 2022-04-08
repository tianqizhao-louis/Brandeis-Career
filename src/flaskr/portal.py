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

    fetch_table = None
    if table_type == 'professor':
        fetch_table = database_server.get_professor_table_all()
        return render_template("admin/table_render.html",
                               table_type=fetch_table["table_name"],
                               fetch_table=fetch_table)
    elif table_type == 'gender':
        fetch_table = database_server.get_gender_table_all()
        return render_template("admin/table_render.html",
                               table_type=fetch_table["table_name"],
                               fetch_table=fetch_table)
    elif table_type == 'concentration':
        fetch_table = database_server.get_concentration_table_all()
        return render_template("admin/table_render.html",
                               table_type=fetch_table["table_name"],
                               fetch_table=fetch_table)
    elif table_type == 'job-merged-table':
        fetch_table = database_server.get_job_merged_table_all()
        return render_template("admin/table_render.html",
                               table_type=fetch_table["table_name"],
                               fetch_table=fetch_table)
    elif table_type == 'company':
        fetch_table = database_server.get_company_table_all()
        return render_template("admin/table_render.html",
                               table_type=fetch_table["table_name"],
                               fetch_table=fetch_table)
