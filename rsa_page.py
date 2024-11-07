"""
Pagina del algoritmo de RSA
"""

import streamlit as st


def app(rsa):
    st.title("Criptado RSA")

    st.write(
        f"""En esta página puedes probar el algoritmo de RSA para encriptación y desencriptación,
            si quieres realizar la comprobación por tu cuenta de los reusltados presentados, las llaves privadas
            y públicas se dan a continuación.

            \n\n
            Llave pública (e,n) = ({rsa.e}, {rsa.n})\t Llave privada (d, n) = ({rsa.d}, {rsa.n})
        """
    )

    st.write(
        """
        Instrucciones: Para este programa únicamente puedes ingresar numeros, para encriptar o desencriptar varios numeros
        a la vez ingresa los numeros separados por una coma, ejemplo: 101,134,157
        """
    )

    cifrado, descifrado = st.columns(2)

    with cifrado:
        st.header("Encriptación")
        text_input = st.text_input("Introduce el mensaje a cifrar: ")

        if text_input:
            mensaje_cifrado = rsa.encriptar(text_input)

            if mensaje_cifrado == -1:
                st.write(
                    "El mensaje no tiene el formato adecuado, ingresa solo numeros separados por coma"
                )
            else:
                st.write(f"El mensaje cifrado es {mensaje_cifrado}")

    with descifrado:
        st.header("Desencriptación")
        text_input = st.text_input("Introduce el mensaje a decifrar: ")

        if text_input:
            mensaje_descifrado = rsa.desencriptar(text_input)

            if mensaje_descifrado == -1:
                st.write(
                    "El mensaje no tiene el formato valido, ingresa solo numeros separados por coma"
                )
            else:
                st.write(f"El mensaje descifrado es {mensaje_descifrado}")
