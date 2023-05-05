"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaapnm7avj5o49dlb2g-a.oregon-postgres.render.com",
        database="todo_wtf0",
        user="root",
        password="BBYTm2flsksDV1yVYJk4UyoumNgXADZL")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
