from flask_restful import Resource
from Models.ventas import Ventas
from Models.productos import Productos
from Controller.productocontroller import ProductoController
from Controller.ingredientecontroller import IngredienteController
from db import db

class VentaController(Resource):
    
    def actualizar_ventas(self, id_producto:object)->None:
        productoController=ProductoController()
        producto=Productos.query.filter_by(id=id_producto).first()
        nombre_producto=producto.nombre
        tipo_producto=producto.tipo
        dinero_venta=producto.precio_publico
        calorias_producto=productoController.obtener_calorias()[id_producto-1]
        precios__ingred=productoController.obtener_lista_precios_ingredientes(id_producto=id_producto)
        rentabilidad=productoController.calcular_rentabilidad(lista_precios_ingred=precios__ingred,precio_venta=dinero_venta)
        
        ### Adición de los datos a la tabla de ventas
        venta = Ventas(id_producto=id_producto, nombre_producto=nombre_producto, tipo_producto=tipo_producto, dinero_venta=dinero_venta,
                       calorias_producto=calorias_producto, costo_producto=sum(precios__ingred), rentabilidad=rentabilidad, )
        db.session.add(venta)
        db.session.commit()
    
    def vender(self , id_producto: int)->list[bool, list]:
        producto_controller=ProductoController()
        ingredientes_controller=IngredienteController()
        
        lista_ingredientes=producto_controller.ingredientes(id_producto=id_producto)
        lista_inventario_vacios=ingredientes_controller.control_inventario(lista_ingredientes=lista_ingredientes)
        
        if len(lista_inventario_vacios)==0:
            self.actualizar_ventas(id_producto=id_producto)
            ingredientes_controller.gastar_ingrediente(lista_ingredientes=lista_ingredientes)
            return True, lista_inventario_vacios
        else:
            return False, lista_inventario_vacios
    