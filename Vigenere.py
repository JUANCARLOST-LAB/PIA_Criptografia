"""
En este programa implementaremos una clase para realizar el cifrado vigenere
"""

from typing import List, Dict


class Vigenere:

    clave: str = ""
    letras_a_valor: Dict[str, int] = {}
    valor_a_letras: Dict[int, str] = {}
    posicion_actual: int = 0

    def __init__(self):
        self.clave = "FISICOMATEMATICO"

        for valor in range(ord("A"), ord("Z") + 1):
            self.letras_a_valor[chr(valor)] = valor - ord("A")
            self.valor_a_letras[valor - ord("A")] = chr(valor)

    def encriptar(self, mensaje: str) -> str:
        mensaje = mensaje.upper()

        self.posicion_actual = 0

        mensaje_encriptado: str = ""

        for letra in mensaje:

            if ord("A") <= ord(letra) <= ord("Z"):
                mensaje_encriptado += self.encriptar_letra(letra)
            else:
                mensaje_encriptado += letra

        return mensaje_encriptado

    def encriptar_letra(self, letra: str) -> str:
        valor: int = self.letras_a_valor[letra]

        letra_clave_actual: str = self.clave[self.posicion_actual]
        valor_clave: int = self.letras_a_valor[letra_clave_actual]

        nueva_posicion: int = (valor + valor_clave) % len(self.letras_a_valor)

        self.posicion_actual = (self.posicion_actual + 1) % len(self.clave)

        return self.valor_a_letras[nueva_posicion]

    def desencriptar(self, mensaje: str) -> str:
        mensaje = mensaje.upper()
        self.posicion_actual = 0

        mensaje_desencriptado: str = ""

        for letra in mensaje:

            if ord("A") <= ord(letra) <= ord("Z"):
                mensaje_desencriptado += self.desencriptar_letra(letra)
            else:
                mensaje_desencriptado += letra

        return mensaje_desencriptado

    def desencriptar_letra(self, letra: str) -> str:
        valor: int = self.letras_a_valor[letra]

        letra_clave_actual: str = self.clave[self.posicion_actual]
        valor_clave: int = self.letras_a_valor[letra_clave_actual]

        nueva_posicion: int = (valor - valor_clave + len(self.letras_a_valor)) % len(
            self.letras_a_valor
        )

        self.posicion_actual = (self.posicion_actual + 1) % len(self.clave)

        return self.valor_a_letras[nueva_posicion]
