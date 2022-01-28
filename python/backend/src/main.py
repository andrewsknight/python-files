# importamos la librería flask y la guardamos en la libreria Flask
from flask import Flask, jsonify, request
from utils.dataBase import saveUser
from flask_cors import CORS


# Creamos una variable app que contiene el servirdor de Flask
app = Flask(__name__)
CORS(app)
# CRUD
# Create => POST
# Read => GET
# Update => PUT
# Delete => DELETE

 
@app.route('/',methods = ['GET'])
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
    saveUser(user)
    return jsonify(user)


app.run('0.0.0.0')