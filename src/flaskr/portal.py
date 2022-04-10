import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from .db import Database

bp = Blueprint('portal', __name__)


@bp.route('/admin', methods=['GET'])
def admin():
    return render_template("admin/admin_home.html")


@bp.route('/admin/table/<string:table_type>', methods=['GET'])
def render_table(table_type):
    database_server = Database(host=current_app.config["MYSQL_HOST"],
                               port=current_app.config["MYSQL_PORT"],
                               user=current_app.config["MYSQL_USER"],
                               password=current_app.config["MYSQL_PASSWORD"],
                               database=current_app.config["MYSQL_DATABASE"])

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


@bp.route('/admin/table/insert/<string:table_type>', methods=["GET"])
def insert_new_record(table_type):
    database_server = Database(host=current_app.config["MYSQL_HOST"],
                               port=current_app.config["MYSQL_PORT"],
                               user=current_app.config["MYSQL_USER"],
                               password=current_app.config["MYSQL_PASSWORD"],
                               database=current_app.config["MYSQL_DATABASE"])
    if table_type == 'professor':
        return render_template("admin/table_insert.html",
                               table_type=table_type)


@bp.route('/admin/table/insert/ajax/<string:table_type>', methods=["POST"])
def ajax_insert_new_record(table_type):
    database_server = Database(host=current_app.config["MYSQL_HOST"],
                               port=current_app.config["MYSQL_PORT"],
                               user=current_app.config["MYSQL_USER"],
                               password=current_app.config["MYSQL_PASSWORD"],
                               database=current_app.config["MYSQL_DATABASE"])
    if table_type == 'professor':
        request.get_data()
        json_data = request.json

        flat_list = [json_data["firstName"], json_data["lastName"]]
        inserted_id = database_server.insert_into_professor_table(flat_list)

        return {
            "database_status": "Success",
            "inserted_id": inserted_id
        }
