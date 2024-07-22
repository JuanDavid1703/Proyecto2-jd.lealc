from flask_sqlalchemy import SQLAlchemy
from db import db
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from Controller.productocontroller import ProductoController
from Controller.ventacontroller import VentaController
from Controller.ingredientecontroller import IngredienteController
from Models.productos import Productos
from Models.ingredientes import Ingredientes

user_name="root"
pasw="Temporal123*"
server="localhost"
data_base="proyecto2"

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql://{user_name}:{pasw}@{server}/{data_base}"
db.init_app(app)
api=Api(app)


@app.route("/")
def main():
    return render_template("Bienvenida.html") 


@app.route("/menu", methods=["GET","POST"])
def venta():
    producto_controller=ProductoController()
    venta_controller=VentaController()
    if request.method == 'GET':
        productos_sql=Productos.query.all()
        return render_template("Menu.html", productos=zip(productos_sql, producto_controller.obtener_lista_productos(), 
                                                   producto_controller.obtener_calorias()))
    else:
        id_producto = request.form['id']
        producto = Productos.query.filter_by(id=id_producto).first()
        venta,lista_inventario_vacios=venta_controller.vender(producto.id)
        if venta==True:
            return render_template("Venta_exitosa.html", producto_vendido=producto)
        else:
            return render_template("Venta_fallida.html", inventario_vacio=lista_inventario_vacios)
            

@app.route("/inventario", methods=["GET","POST"])
def reabastecer():
    ingredientecontroller=IngredienteController()
    if request.method == 'GET':
        ingredientes=Ingredientes.query.all()
        return render_template("inventario.html",ingredientes=ingredientes)
    else:
        id_abastecimiento_ing=0
        id_abastecimiento_ing = request.form['id_abastecer']
        
        if int(id_abastecimiento_ing)>0:
            ingredientecontroller.abastecer(id_ingrediente=id_abastecimiento_ing)
            nombre_ingrediente_abastecido=Ingredientes.query.filter_by(id=id_abastecimiento_ing).first().nombre
            return render_template("reabastecer.html", nombre_ingrediente=nombre_ingrediente_abastecido)

if __name__=="__app__":
    app.run(debug=True)
    
    
    
    