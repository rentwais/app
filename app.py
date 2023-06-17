# Importa las bibliotecas y funciones necesarias
from flask import Flask, render_template, request
from sklearn.preprocessing import OneHotEncoder
import pickle as cPickle
import numpy as np
import datetime
# Importa archivo con datos aparte para no incluirlos en este principal
from configData import *

# inicializamos el framework
app = Flask(__name__)

# Ruta principal del sitio web
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir el formulario y mostrar la predicción
@app.route('/predict', methods=['POST'])
def predict():

    # Se obtienen los valores enviados desde el formulario
    localidad = request.form['localidad']

    # como distrito va relacionado con barrio (localidad), ya no se recibe por formulario
    # sino que se 'mapea' en 'barrios' para obtener el distrito de cada barrio.
    distrito = barrios[request.form['localidad']]

    planta = int(request.form['planta'])
    metros = int(request.form['metros'])
    habitaciones = int(request.form['habitaciones'])
    banos = int(request.form['banos'])
    ascensor = request.form['ascensor']
    aire_acondicionado = request.form['aire_acondicionado']
    exterior = request.form['exterior']
    amueblada = request.form['amueblada']
    tipovivienda = request.form['tipovivienda']
    calefaccion = request.form['calefaccion']
    
    # Se carga el modelo entrenado previamente: rfModel
    with open('rfModel.pckl', 'rb') as f:
        model = cPickle.load(f)

    # Convertir distrito y barrio en keys similares al One Hot Encoder (distrito_centro, localidad_sol)
    key_distrito = 'distrito_' + distrito
    key_localidad = 'localidad_' + localidad

    # se crea una lista de valores conocidos 
    datos_conocidos = {
        'metros': metros,
        'habitaciones': habitaciones,
        'baños': banos,
        'exterior': exterior,
        'equipada': 1,
        'amueblada': amueblada,
        'planta': planta,
        'ascensor': ascensor,
        key_distrito: 1,
        key_localidad: 1
    }

    # para la prediccion se necesitan 167 parametros (numero_parametros) asi que se debe
    # crear un vector de características con todas las características establecidas en 0
    vector = np.zeros(numero_parametros)

    # Actualizar el vector de características con los valores conocidos
    for feature, valor in datos_conocidos.items():
        if feature in features:
            indice = features.index(feature)
            vector[indice] = valor

    # Se realiza la predicción utilizando la lista con valores actualizados
    prediction = model.predict([vector])

    # guardar la fecha y hora de la consulta para mostrarla
    fecha=datetime.datetime.now()

    # Datos que serán enviados como "response" al template "result"
    datos = {
        'metros': metros,
        'habitaciones': habitaciones,
        'distrito': distrito,
        'localidad': localidad,
        'tipo': tipovivienda
    }

    # Renderiza el template 'result.html' y pasa la predicción como variable
    # la prediccion es un array con 1 elemento, se pasa el primer y unico elemento [0]
    # además se envian la fecha y los datos para referencia del usuario.
    return render_template('result.html', prediction=prediction[0], fecha=fecha, datos=datos)

if __name__ == '__main__':
    app.run()