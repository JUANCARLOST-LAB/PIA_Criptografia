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
    st.write(
        """
            El cifrado de Vigenère es un método de encriptación polialfabético que usa una clave 
            para cifrar el texto de forma más segura que un cifrado de César simple. Cada letra 
            del texto plano se cifra utilizando un desplazamiento determinado por la letra 
            correspondiente de la clave. Por ejemplo, si la clave es 'KEY' y el texto es 'HELLO', 
            cada letra del texto se cifra con la posición de la letra de la clave.

            **Ejemplo sencillo**:
            Texto: `HELLO`
            Clave: `KEY`

            1. Emparejamos el texto y la clave repetidamente: `KEYKE`
            2. Convertimos las letras a números (A = 0, B = 1, ..., Z = 25):
            - Texto: H(7), E(4), L(11), L(11), O(14)
            - Clave: K(10), E(4), Y(24), K(10), E(4)

            3. Ciframos cada letra sumando los valores del texto y la clave, módulo 26:
            - H + K = (7 + 10) % 26 = 17 → R
            - E + E = (4 + 4) % 26 = 8 → I
            - L + Y = (11 + 24) % 26 = 9 → J
            - L + K = (11 + 10) % 26 = 21 → V
            - O + E = (14 + 4) % 26 = 18 → S

            Texto cifrado: `RIJVS`
             """
    )

    st.header("Metodo RSA")
    st.write(
        """
        RSA es un algoritmo de cifrado asimétrico que utiliza un par de claves: una clave 
        pública para encriptar datos y una clave privada para desencriptarlos. Este método 
        se basa en la dificultad de factorizar grandes números compuestos de dos números 
        primos. RSA es ampliamente utilizado en la seguridad informática moderna para el 
        intercambio seguro de datos y firmas digitales.

        **Ejemplo sencillo**:
        1. Elegimos dos números primos, p = 3 y q = 11.
        2. Calculamos n = p × q = 3 × 11 = 33.
        3. Calculamos φ(n) = (p - 1) × (q - 1) = 2 × 10 = 20.
        4. Elegimos un exponente público e tal que 1 < e < φ(n) y que sea coprimo con φ(n), 
        por ejemplo, e = 3.
        5. Calculamos el exponente privado d tal que (e × d) % φ(n) = 1, obteniendo d = 7.

        **Cifrado**:
        Para cifrar el número m = 4, calculamos:
        c = m^e % n = 4^3 % 33 = 64 % 33 = 31.

        **Desencriptado**:
        Para desencriptar c = 31, calculamos:
        m = c^d % n = 31^7 % 33 = 4.

        El número original, 4, se recupera correctamente.
        """
    )
