from Controller.ingredientecontroller import IngredienteController
from Models.ingredientes import Ingredientes
from db import db
import unittest

### python -m unittest Tests.test_ingrediente

class Test_ingredientes(unittest.TestCase):
    def test_es_sano(self):
        ingredientecontroller=IngredienteController()
        self.assertEqual(ingredientecontroller.es_sano(id_ingrediente=9),True)
    
    def test_abastecer(self):
        ingredientecontroller=IngredienteController()
        ingredientes=Ingredientes.query.filter_by(id=2).first()
        tipo=ingredientes.tipo
        print(tipo)
        inventario=ingredientes.inventario
        print(inventario)
        
        if tipo=="Base":
            self.assertEqual(ingredientecontroller.abastecer(id_ingrediente=2),inventario+5)
        if tipo=="Complemento":
            self.assertEqual(ingredientecontroller.abastecer(id_ingrediente=2),inventario+10)
    
    def test_abastecer(self):
        ingredientecontroller=IngredienteController()
        ingredientes=Ingredientes.query.filter_by(id=2).first()
        inventario=ingredientes.inventario
        tipo=ingredientes.tipo
        if tipo=="Base":
            self.assertEqual(ingredientecontroller.renovar_inventario_complemento(id_ingrediente=2),"No se puede renovar un base")
        if tipo=="Complemento":
            self.assertEqual(ingredientecontroller.renovar_inventario_complemento(id_ingrediente=2),"Éxito")
        

if __name__=="__main__":
    unittest.main()