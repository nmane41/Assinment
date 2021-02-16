import flask
#
# from sqlobject import *
# import os
# import student
# import backlog
# import requests
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
#
#
# @app.route('/', methods=['GET'])
# def home():
#     # db_connection()
#     return "Nitin"
#
#
# @app.route('/createdb', methods=['GET'])
# def create_db():
#     db_connection()
#     student.Student.createTable(ifNotExists=True)
#     backlog.Backlog.createTable(ifNotExists=True)
#     return 'db created'
#
#
# @app.route('/add', methods=['POST'])
# def insert_data():
#     try:
#         db_connection()
#         data=flask.request.json
#         val = student.Student.select(student.Student.get(id))
#
#         #check =  val["student_info.id"]
#         print(val)
#         #student.Student(firstName=data["firstName"], lastName=data["lastName"], address=data["address"])
#
#         #backlog.Backlog(backlog_count=data["b_count"],student_id=)
#         return "Data inserted"
#     except Exception as e:
#         return e
#
#
# def db_connection():
#     # from tool import app
#
#     db_file = os.path.abspath('student_details.db')
#     connection_string = 'sqlite:' + db_file
#     connection = connectionForURI(connection_string)
#     sqlhub.processConnection = connection
#
#
#
# app.run()

app = flask.Flask(__name__)