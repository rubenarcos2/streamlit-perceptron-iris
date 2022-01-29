import streamlit as st
from scipy.io import arff
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report
import os

def second_page():
    text = """
            # ¿Cómo funciona el clasificador?
            """
    st.write(text)

    st.write("Carga del dataset desde un fichero externo")
    st.code("df_raw = arff.loadarff('iris.arff')")
    st.code("df = pd.DataFrame(df_raw[0])")

    #Esto es necesario para encontrar el path de los ficheros en heroku
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Comentar al iniciar en local
    # Load the data using "iris.loadarff" then convert it to dataframe
    df_raw = arff.loadarff(os.path.join(BASE_DIR, 'src/iris.arff')) #Comentar al iniciar en local
    #df_raw = arff.loadarff('iris.arff') #Desomentar al iniciar en local
    df = pd.DataFrame(df_raw[0])
    st.dataframe(df)

    st.write("Paso a categórica la columna 'class' y la codifico en utf-8 por que venía en unicode para poder trabaja ")
    st.code("df['class'] = pd.Categorical(df['class'])")
    st.code("df['class'] = df['class'].str.decode('utf-8')")

    df["class"] = pd.Categorical(df["class"])
    df["class"] = df['class'].str.decode("utf-8")

    st.write("\nMatriz de correlación")
    st.code("df.corr()")
    st.write(df.corr())

########################################################################################################################

    st.write("## Clasificador Pab")
    st.write("Vamos a crear el primer perceptron (Pab) para la clasificación de las dos primeras clases.")
    st.write("\t- Iris-setosa")
    st.write("\t- Iris-versicolor")
    st.write("Este es el conjunto de datos que le vamos a pasar al perceptrón para que nos lo clasifique")

    st.code("Pab = df[(df['class'] != 'Iris-virginica')]")
    st.code("y = Pab['class']")
    st.code("x = Pab.drop(['class'], axis=1)")

    Pab = df[(df['class'] != "Iris-virginica")]
    st.write(Pab)
    y = Pab["class"]
    x = Pab.drop(["class"], axis=1)

    st.code("pab = Perceptron(random_state=42,"
            "       max_iter=100,"
            "       tol=0.001)")
    pab = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pab.fit(x, y)
    st.write("Salida del entrenamiento")
    st.write(pab.fit(x, y))

    st.write("Reporte de clasificación")
    st.code("print(classification_report(pab.predict(x), y))")
    st.write(classification_report(pab.predict(x), y))

########################################################################################################################

    st.write("## Clasificador Pbc")
    st.write("Vamos a crear el primer perceptron (Pbc) para la clasificación de las dos primeras clases.")
    st.write("\t- Iris-versicolor")
    st.write("\t- Iris-virgínica")
    st.write("Este es el conjunto de datos que le vamos a pasar al perceptrón para que nos lo clasifique")

    st.code("Pbc = df[(df['class'] != 'Iris-setosa')]")
    st.code("y = Pab['class']")
    st.code("x = Pab.drop(['class'], axis=1)")

    Pbc = df[(df['class'] != "Iris-setosa")]
    st.write(Pbc)
    y = Pbc["class"]
    x = Pbc.drop(["class"], axis=1)

    st.code("pbc = Perceptron(random_state=42,"
            "       max_iter=100,"
            "       tol=0.001)")
    pbc = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pbc.fit(x, y)
    st.write("Salida del entrenamiento")
    st.write(pbc.fit(x, y))

    st.write("Reporte de clasificación")
    st.code("print(classification_report(pbc.predict(x), y))")
    st.write(classification_report(pbc.predict(x), y))

########################################################################################################################

    st.write("## Clasificador Pac")
    st.write("Vamos a crear el primer perceptron (Pac) para la clasificación de las dos primeras clases.")
    st.write("\t- Iris-setosa")
    st.write("\t- Iris-virgínica")
    st.write("Este es el conjunto de datos que le vamos a pasar al perceptrón para que nos lo clasifique")

    st.code("Pac = df[(df['class'] != 'Iris-versicolor')]")
    st.code("y = Pac['class']")
    st.code("x = Pac.drop(['class'], axis=1)")

    Pac = df[(df['class'] != "Iris-versicolor")]
    st.write(Pac)
    y = Pac["class"]
    x = Pac.drop(["class"], axis=1)

    st.code("pac = Perceptron(random_state=42,"
            "       max_iter=100,"
            "       tol=0.001)")
    pac = Perceptron(random_state=42,
                     max_iter=100,
                     tol=0.001)
    pac.fit(x, y)
    st.write("Salida del entrenamiento")
    st.write(pac.fit(x, y))

    st.write("Reporte de clasificación")
    st.code("print(classification_report(pac.predict(x), y))")
    st.write(classification_report(pac.predict(x), y))

########################################################################################################################

