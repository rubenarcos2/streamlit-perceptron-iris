import streamlit as st

from page_sidebar import sidebar
from page_front import front
from page_second import second_page
from page_prediction import predictor

def main():

    pages_mapper = {
                        'Inicio': front,
                        '¿Cómo funciona el clasificador?': second_page,
                        'Predictor': predictor,
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()