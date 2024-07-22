from flask_restful import Resource
from Models.ingredientes import Ingredientes
from db import db

class IngredienteController(Resource):       
    def gastar_ingrediente(self,lista_ingredientes: list[int,int,int])->None:
        for id_ing in lista_ingredientes:
            ingrediente=Ingredientes.query.filter_by(id=id_ing).first()
            ingrediente.inventario=ingrediente.inventario-1
            db.session.commit()
    
    def control_inventario(self, lista_ingredientes: list)->list:
        nombre_ingred_vacio=[]
        for id_ingrediente in lista_ingredientes:
            inventario=Ingredientes.query.filter_by(id=id_ingrediente).first().inventario
            if inventario==0:
                nombre_ingred_vacio.append(Ingredientes.query.filter_by(id=id_ingrediente).first().nombre)
        return nombre_ingred_vacio
    
    def es_sano(self, id_ingrediente: int)->bool:
        caloria_ingediente=Ingredientes.query.filter_by(id=id_ingrediente).first().calorias
        es_vegeteriano=Ingredientes.query.filter_by(id=id_ingrediente).first().es_vegetariano
        if caloria_ingediente<200 or es_vegeteriano=="Si":
            return True
        else:
            return False
    
    def abastecer(self,id_ingrediente: int)->None:
        ingrediente=Ingredientes.query.filter_by(id=id_ingrediente).first()
        
        if ingrediente.tipo=="Base":
            ingrediente.inventario=ingrediente.inventario+5
            db.session.commit()
        
        if ingrediente.tipo=="Complemento":
            ingrediente.inventario=ingrediente.inventario+10
            db.session.commit()
    
    def renovar_inventario_complemento(self,id_ingrediente:int)->str:
        ingrediente=Ingredientes.query.filter_by(id=id_ingrediente).first()
        if ingrediente.tipo=="Complemento":
            ingrediente.inventario=0
            return "Éxito"
        else:
            return "No se puede renovar un base"