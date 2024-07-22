from db import db
from flask_sqlalchemy import SQLAlchemy
from Models.productos import Productos

class Ventas(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    id_producto=db.Column(db.Integer,db.ForeignKey("productos.id"), nullable=False)
    nombre_producto=db.Column(db.String(45), nullable=False)
    tipo_producto=db.Column(db.String(45), nullable=False)
    dinero_venta=db.Column(db.Float(2), nullable=False)
    calorias_producto=db.Column(db.Float(2), nullable=False)
    costo_producto=db.Column(db.Float(2), nullable=False)
    rentabilidad=db.Column(db.Float(2), nullable=False)
    producto=db.relationship('Productos', backref="productos", lazy=True)
    
    