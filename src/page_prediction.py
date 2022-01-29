import streamlit as st
from scipy.io import arff
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report
import os

def prediction(sepal_length, sepal_width, petal_length, petal_width):
    #Esto es necesario para encontrar el path de los ficheros en heroku
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Comentar al iniciar en local
    # Load the data using "iris.loadarff" then convert it to dataframe
    df_raw = arff.loadarff(os.path.join(BASE_DIR, 'src/iris.arff')) #Comentar al iniciar en local
    #df_raw = arff.loadarff('iris.arff') #Desomentar al iniciar en local
    df = pd.DataFrame(df_raw[0])

    df["class"] = pd.Categorical(df["class"])
    df["class"] = df['class'].str.decode("utf-8")

    Pab = df[(df['class'] != "Iris-virginica")]
    y = Pab["class"]
    x = Pab.drop(["class"], axis=1)

    pab = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pab.fit(x, y)

    Pbc = df[(df['class'] != "Iris-setosa")]
    y = Pbc["class"]
    x = Pbc.drop(["class"], axis=1)

    pbc = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pbc.fit(x, y)

    Pac = df[(df['class'] != "Iris-versicolor")]
    y = Pac["class"]
    x = Pac.drop(["class"], axis=1)

    pac = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pac.fit(x, y)

    #Construcción del array con los datos introducidos
    a = np.array([sepal_length, sepal_width, petal_length, petal_width])
    a = a.reshape(1, -1)

    out = ""
    # Para el perceptrón Pab
    pred_pab = pab.predict(a)
    pred_pbc = pbc.predict(a)
    pred_pac = pac.predict(a)

    pred_enAenBenC = np.array([False, False, False])

    if pred_pab == 'Iris-setosa' or pred_pac == 'Iris-setosa':
        pred_enAenBenC[0] = True
    if pred_pab == 'Iris-versicolor' or pred_pbc == 'Iris-versicolor':
        pred_enAenBenC[1] = True
    if pred_pac == 'Iris-virginica' or pred_pbc == 'Iris-virginica':
        pred_enAenBenC[2] = True

    # En los casos de duplicidad de clases
    if pred_enAenBenC[0] and pred_enAenBenC[1] and not pred_enAenBenC[2]:
        out = pab.predict(a)
    if not pred_enAenBenC[0] and pred_enAenBenC[1] and pred_enAenBenC[2]:
        out = pbc.predict(a)
    if pred_enAenBenC[0] and not pred_enAenBenC[1] and pred_enAenBenC[2]:
        out = pac.predict(a)


    return out

def predictor():
    st.title("Predictor del tipo de flor iris")
    st.write("Introduciendo los valores de medición de una flor iris, se va ha predecir la clase a la que pertenece.")

    sepal_length = st.text_input("Sepal Length", "Introduzca un valor...")
    sepal_width = st.text_input("Sepal Width", "Introduzca un valor...")
    petal_length = st.text_input("Petal Length", "Introduzca un valor...")
    petal_width = st.text_input("Petal Width", "Introduzca un valor...")
    result = ""

    if st.button("Predecir la clase a la que pertenece"):
        result = prediction(sepal_length, sepal_width, petal_length, petal_width)
    st.success('Los datos introducidos pertenecen a la flor {}.'.format(result))