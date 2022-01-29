import streamlit as st


def sidebar(ls_page_name):

    # Resources
    edition = "Barra lateral"
    title = "## Selecciona la navegación"
    description = "Menú 1 seleccionado y mostrado por defecto"

    st.sidebar.write(edition)
    st.sidebar.write(title)
    st.sidebar.write(description)
    page_name = st.sidebar.selectbox("", ls_page_name)

    return page_name