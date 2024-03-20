import sqlite3

from flask import Flask

db = sqlite3.connect("data.db")


def authentication(app: Flask):
    @app.post("/login")
    def login():
        return "Login"
