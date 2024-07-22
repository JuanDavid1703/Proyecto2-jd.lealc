from Controller.ingredientecontroller import IngredienteController
from Controller.productocontroller import ProductoController
from Models.ingredientes import Ingredientes
from Models.productos import Productos
from db import db
import unittest

### python -m unittest Tests.test_producto

class Test_productos(unittest.TestCase):
    def test_calcular_calorias(self):
        ingredientecontroller=IngredienteController()
        productocontroller=ProductoController()
        producto=Productos.query.filter_by(id=4)
        id_ing_por_producto=[producto.id_ingred1,producto.id_ingred2,producto.id_ingred3]
        calorias_ingr_por_prodcuto=[]
        for ing in id_ing_por_producto:
                i=Ingredientes.query.filter_by(id=ing).first()
                calorias_ingr_por_prodcuto.append(i.calorias)
        self.assertEqual(productocontroller.calcular_calorias(lista_calorias=calorias_ingr_por_prodcuto,tipo=producto.tipo),2150)
    
    def test_calcular_costo(self):
        productocontroller=ProductoController() 
        lista_precios=productocontroller.obtener_lista_precios_ingredientes(id_producto=6)
        self.assertEqual(productocontroller.calcular_costo(lista_precios_ingredientes=lista_precios),sum(lista_precios))
    
    def test_calcular_rentabilidad(self):
        productocontroller=ProductoController() 
        producto=Productos.query.filter_by(id=3).first()
        lista_precios=productocontroller.obtener_lista_precios_ingredientes(id_producto=6)
        costo_total=sum(lista_precios)
        precio_producto=producto.precio_publico
        self.assertEqual(productocontroller.calcular_rentabilidad (precios=costo_total,precio_venta=precio_producto),precio_producto-costo_total)
    
    def test_producto_mas_rentable(self):
        productocontroller=ProductoController() 
        producto=Productos.query.all()
        lista_precios=producto.precio_publico
        lista_nombre_productos=productocontroller.obtener_lista_productos()
        self.assertEqual(productocontroller.mejor_producto(lista_nombre_prodcutos=lista_nombre_productos,lista_precios=lista_precios),"Chocomalteada")    

if __name__=="__main__":
    unittest.main()