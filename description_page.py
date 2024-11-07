import streamlit as st


def app():
    st.title("Presentación")

    st.write(
        """
             Hola! La presente página fue diseñada por el alumno Juan Carlos Tapia Baeza
             para la materia de Criptografía y Seguridad impartida por el profesor Angel
             Salvador Perez Blanco, en este página se pondrán a prueba dos métodos para 
             encriptar y desencriptar mensajes que fueron seleccionadas por un servidor, 
             los métodos que decidí seleccionar fueron los métodos criptográficos
             Vigenere y RSA, a continuación explicaré cómo funcionan cada uno.
             """
    )

    st.header("Método Vigenere")
