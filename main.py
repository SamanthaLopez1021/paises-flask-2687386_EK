"""Importar flask"""
from flask import Flask
"""Variable app, toma valor de flask por nombre """
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hola Python'
