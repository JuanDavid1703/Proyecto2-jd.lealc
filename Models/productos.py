from db import db
from flask_sqlalchemy import SQLAlchemy
from Models.ingredientes import Ingredientes
# from Models.ventas import Ventas

class Productos(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    tipo=db.Column(db.String(45), nullable=False)
    nombre=db.Column(db.String(45), nullable=False)
    precio_publico=db.Column(db.Float(2), nullable=False)
    volumen_oz=db.Column(db.Float(2), nullable=False)
    tipo_vaso=db.Column(db.String(45), nullable=False)
    id_ingred1=db.Column(db.Integer, nullable=False)
    id_ingred2=db.Column(db.Integer, nullable=False)
    id_ingred3=db.Column(db.Integer, nullable=False)
    

    

       