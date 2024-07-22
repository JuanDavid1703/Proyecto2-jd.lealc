from flask_restful import Resource
from Models.ingredientes import Ingredientes
from Models.productos import Productos
from db import db

class ProductoController(Resource):
    def __init__(self) -> None:
        self._Lista_productos=[]
        self._Calorias_productos=[]
    
    def obtener_lista_productos(self):
        productos = Productos.query.all()
        self._Lista_productos=[]
        for k, producto in enumerate(productos):
            id_ing_por_producto=[producto.id_ingred1,producto.id_ingred2,producto.id_ingred3]
            nombre_ingr_por_prodcuto=[]
            
            for ing in id_ing_por_producto:
                i=Ingredientes.query.filter_by(id=ing).first()
                nombre_ingr_por_prodcuto.append(i.nombre)

            self._Lista_productos.append(", ".join(nombre_ingr_por_prodcuto))
        return self._Lista_productos
    
    def obtener_lista_precios_ingredientes(self, id_producto:int)->list:
        producto = Productos.query.filter_by(id=id_producto).first()
        id_ing_por_producto=[producto.id_ingred1,producto.id_ingred2,producto.id_ingred3]
        precios_ingr_por_producto=[]
            
        for ing in id_ing_por_producto:
            i=Ingredientes.query.filter_by(id=ing).first()
            precios_ingr_por_producto.append(i.precio)
        return precios_ingr_por_producto
    
    
    def calcular_calorias(self, lista_calorias: list, tipo:str)->float:
        if tipo=="Copa":
            return round(sum(lista_calorias)*0.95,2)
        if tipo=="Malteada":
            return sum(lista_calorias)+200
    
    
    def calcular_costo(self, lista_precios_ingredientes: list[float, float, float])->float:
        precio_total=0
        for precio in lista_precios_ingredientes:
            precio_total+=precio
        return precio_total
    
    def obtener_calorias(self)->list:
        productos = Productos.query.all()
        self._Calorias_productos=[]
        for k, producto in enumerate(productos):
            id_ing_por_producto=[producto.id_ingred1,producto.id_ingred2,producto.id_ingred3]
            calorias_ingr_por_prodcuto=[]
            
            for ing in id_ing_por_producto:
                i=Ingredientes.query.filter_by(id=ing).first()
                calorias_ingr_por_prodcuto.append(i.calorias)
            
            self._Calorias_productos.append(self.calcular_calorias(lista_calorias=calorias_ingr_por_prodcuto,tipo=producto.tipo))
        return self._Calorias_productos

    def calcular_rentabilidad(self,lista_precios_ingred: list, precio_venta: float)->float:
        costo_prod=self.calcular_costo(lista_precios_ingredientes=lista_precios_ingred)
        return precio_venta-costo_prod
    
    def mejor_producto(self,lista_nombre_prodcutos: list,lista_precios: list)->str:
        lista_rentabilidad=[]
        for k, precio in enumerate(lista_precios):
            lista_precios_por_producto=self.obtener_lista_precios_ingredientes(id_producto=k)
            lista_rentabilidad.append(self.calcular_rentabilidad(lista_precios_ingred=lista_precios_por_producto,precio_venta=precio))
        
        mas_rentable=lista_rentabilidad[0]
        for k, prod in enumerate(lista_nombre_prodcutos[1:]): 
            if prod[k]>precio_rentable:
                mas_rentable=lista_nombre_prodcutos[k]
                precio_rentable=lista_rentabilidad[k]
        return mas_rentable

    
    def ingredientes(self, id_producto:int)->list:
        producto=Productos.query.filter_by(id=id_producto).first()
        return [producto.id_ingred1,producto.id_ingred2,producto.id_ingred3]