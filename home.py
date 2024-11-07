import streamlit as st
import description_page
import vigenere_page
import rsa_page
from Vigenere import Vigenere
from RSA import RSA

# Instancias de clases para usar
vigenere = Vigenere()
rsa = RSA()


def app():
    # Titulo de la app
    st.title("Programas de encriptación")

    # Bienvenida
    st.write(
        """Bienvenido a esta página, donde podrás desencriptar 
        y encriptar mensajes de texto a través de múltiples técnicas 
        de encriptación, selecciona una de las opciones que se 
        muestran a la izquierda para continuar."""
    )

    selection = st.sidebar.radio("Go to", ["Descripcion", "Vigenere", "RSA"])

    if selection == "Descripcion":
        description_page.app()
    elif selection == "Vigenere":
        vigenere_page.app(vigenere)
    elif selection == "RSA":
        rsa_page.app(rsa)


app()
