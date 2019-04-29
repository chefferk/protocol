import os


class Config:
    FLASK_ADMIN_SWATCH = 'flatly'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:WindyMicrobes!@35.238.212.11:5432/protocol'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
