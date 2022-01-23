# importamos la librería flask y la guardamos en la libreria Flask
from flask import Flask, jsonify, request
from utils.dataBase import save

# Creamos una variable app que contiene el servirdor de Flask
app = Flask(__name__)



 
@app.route('/',methods = ['GET','POST'])
def hello_world():
    result = {'msg':'Hello world!'}
    return jsonify(result)


@app.route('/otraruta')
def hello_world2():
    result = {'msg':'Hello world desde otra ruta!'}
    return jsonify(result)

# Esta linea lo que hace es que en el postman http://127.0.0.1:5000/user y method post 
@app.route('/user',methods = ['POST'])
def saveUsers():
    user = request.json
    save(user)
    return jsonify(user)