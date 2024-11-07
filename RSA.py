"""
Esta clase está encargada de encriptar y desencriptar un mensaje
por medio del método de RSA
"""

from typing import List, Dict
import numpy as np


class RSA:
    p: int = 67
    q: int = 47

    def __init__(self):
        self.phi = (self.p - 1) * (self.q - 1)
        self.n = self.p * self.q
        self.e = self.obtain_relative_prime(self.phi)
        self.d = self.computar_inverso(self.e, self.phi)

    def encriptar(self, mensaje: str) -> str:
        try:
            valores: List[str] = mensaje.split(",")
            valores_enteros: List[int] = [int(num) for num in valores]
        except Exception as e:
            return -1
        valores_encriptados: List[str] = [
            str(self.encriptar_un_numero(valor)) for valor in valores_enteros
        ]

        mensaje_encriptado: str = ",".join(valores_encriptados)

        return mensaje_encriptado

    def encriptar_un_numero(self, valor: int) -> int:
        resultado: int = 0

        resultado = self.exponenciacion_binaria(valor, self.e, self.n)

        return resultado

    def GCD(self, first_number: int, second_number: int) -> int:
        if first_number == 0:
            return second_number

        return self.GCD(second_number % first_number, first_number)

    def obtain_relative_prime(self, number: int) -> int:
        list_of_relative_primes: List[int] = []
        for num in range(2, number + 1, 1):
            if self.GCD(num, number) == 1:
                list_of_relative_primes.append(num)

        return list_of_relative_primes[3 * len(list_of_relative_primes) // 4]

    def exponenciacion_binaria(self, base: int, exponente: int, modulo: int) -> int:
        resultado: int = 1

        while exponente > 0:
            if exponente & 1:
                resultado = resultado * base

            base = base * base
            resultado = resultado % modulo
            base = base % modulo

            exponente = exponente // 2

        return resultado

    def computar_inverso(self, number: int, modulo: int) -> int:

        exponente: int = self.logaritmo_discreto(number, modulo) - 1

        return self.exponenciacion_binaria(number, exponente, modulo)

    def logaritmo_discreto(self, base: int, modulo: int) -> int:
        raiz: int = int(np.sqrt(modulo)) + 1

        mapa_valores: Dict[int, int] = {}

        for i in range(1, raiz + 1):
            exp_bin: int = self.exponenciacion_binaria(base, i * raiz, modulo)
            mapa_valores[exp_bin] = i

        for i in range(raiz):
            exp_bin: int = self.exponenciacion_binaria(base, i, modulo)

            if exp_bin in mapa_valores:
                return mapa_valores[exp_bin] * raiz - i

        return 0

    def desencriptar(self, mensaje: str) -> str:
        try:
            valores: List[str] = mensaje.split(",")
            valores_enteros: List[int] = [int(num) for num in valores]
        except Exception as e:
            return -1
        valores_desencriptados: List[str] = [
            str(self.desencriptar_un_numero(valor)) for valor in valores_enteros
        ]

        mensaje_encriptado: str = ",".join(valores_desencriptados)

        return mensaje_encriptado

    def desencriptar_un_numero(self, valor: int) -> int:
        resultado: int = 0

        resultado = self.exponenciacion_binaria(valor, self.d, self.n)

        return resultado

    def imprimir_llave_publica(self):
        print(f"La llave publica (n, e) es ({self.n},{self.e})")

    def imprimir_llave_privada(self):
        print(f"La lave privada es : ({self.n},{self.d})")


# rsa = RSA()

# def prueba():
#     rsa.imprimir_llave_publica()
#     rsa.imprimir_llave_privada()
#     while True:
#         mensaje = str(input("Mensaje: "))

#         if mensaje == "\n":
#             break
#         msj = rsa.encriptar(mensaje)

#         print(f"Mensaje encriptado: {msj}")

#         print(f"Comprobacion: {rsa.desencriptar(msj)}")


# prueba()
