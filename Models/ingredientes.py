from flask_sqlalchemy import SQLAlchemy
from db import db

class Ingredientes(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    nombre=db.Column(db.String(45), nullable=False)
    tipo=db.Column(db.String(45), nullable=False)
    precio=db.Column(db.Float(2), nullable=False)
    calorias=db.Column(db.Float(2), nullable=False)
    es_vegetariano=db.Column(db.String(2), nullable=False)
    inventario=db.Column(db.Integer, nullable=False)
    sabor=db.Column(db.String(45), nullable=True)
            
        
    