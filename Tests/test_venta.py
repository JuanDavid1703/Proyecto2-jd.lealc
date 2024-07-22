from Controller.ingredientecontroller import IngredienteController
from Controller.productocontroller import ProductoController
from Controller.ventacontroller import VentaController
from db import db
import unittest

### python -m unittest Tests.test_producto

class Test_productos(unittest.TestCase):
    def test_vender(self):
        producto_controller=ProductoController()
        ingredientes_controller=IngredienteController()
        
        lista_ingredientes=producto_controller.ingredientes(id_producto=1)
        lista_inventario_vacios=ingredientes_controller.control_inventario(lista_ingredientes=lista_ingredientes)
        if len(lista_inventario_vacios)==0:
            self.assertEqual(VentaController.vender(id_producto=1),[True,[]])
        else:
            self.assertEqual(VentaController.vender(id_producto=1),[False,lista_inventario_vacios])
if __name__=="__main__":
    unittest.main()