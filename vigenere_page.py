import streamlit as st


def app(vigenere):
    st.title("Criptado de vigenere")

    st.write(
        f"""Como información adicional, este cifrado se
              estará realizando con la siguiente clave: {vigenere.clave}"""
    )

    cifrado, descifrado = st.columns(2)

    with cifrado:
        st.header("Encriptación")
        text_input = st.text_input("Introduce el mensaje a cifrar: ")

        if text_input:
            mensaje_cifrado = vigenere.encriptar(text_input)
            st.write(f"El mensaje cifrado es {mensaje_cifrado}")

    with descifrado:
        st.header("Desencriptación")
        text_input = st.text_input("Introduce el mensaje a decifrar: ")

        if text_input:
            mensaje_descifrado = vigenere.desencriptar(text_input)
            st.write(f"El mensaje descifrado es {mensaje_descifrado}")