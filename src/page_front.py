import streamlit as st
import pandas as pd


def front():
    text = """
            # IA - Perceptrón clasificador
            
            A continuación, se muestra el funcionamiento de un clasificador utilizando perceptrones para el 
            [iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

            En la parte inferior, se muestra el dataset iris que está compuesto por:
              - 150 muestras de flores iris
              - Se conoce que:
                - Hay 3 grupos de flores iris setosa, iris versicolor e iris virgínica.
                - Las muestras coinciden con 50 observaciones de cada clase
            """
    st.write(text)