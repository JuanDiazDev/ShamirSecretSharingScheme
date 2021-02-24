import hashlib
import base64
import random
import Polynomial
import sys
from Crypto import Random
from Crypto.Cipher import AES

'''
Clase que se ocupa del proceso de encriptación
'''


class Secret:
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    '''
    Constructor de la clase
    :param key: La contraseña
    '''

    def __init__(self, key):
        self.key = int(hashlib.sha256(key.encode()).hexdigest(), 16)

    '''
    Escribe un archivo con el mensaje encriptado
    :param inp: El archivo con el mensaje a encriptar
    :except IOError
    '''

    def encrypt(self, inp):
        try:
            with open(inp, "r") as raw:
            	secret = raw.read()
            ciphertext = self.encrypt_secret(secret)
            dark = open(inp + ".aes", "w+")
            dark.write(str(ciphertext))
            dark.close()
        except IOError:
            sys.exit("Error leyendo el archivo a encriptar. Asegúrate de que exista.")

    '''
    Escribe un archivo con los fragmentos de la contraseña
    :param t: Número de evaluaciones mínimas para desencriptar
    :param n: Número de evaluaciones totales
    :param frags: El archivo donde se escribirán los fragmentos
    :except IOError
    '''

    def fragments(self, t, n, frags):
        poly = Polynomial.Polynomial(t)
        polynomial = poly.generate(self.key)
        try:
            file = open(frags + ".frags", "w+")
            for i in range(n):
                x = random.randint(1, 1000 * n)
                y = poly.horner(x, polynomial)
                file.write(str(x) + ' ' + str(y) + '\n')
            file.close()
        except IOError:
            sys.exit("Ha ocurrido un error escribiendo el archivo de fragmentos")

    '''
    Encripta el mensaje que se recibe como argumento
    :param raw: El mensaje a encriptar
    :return: El mensaje cifrado en bytes
    '''

    def encrypt_secret(self, raw):
        password = self.key.to_bytes(32, "big")
        raw = Secret.pad(raw)
        raw = raw.encode()
        if len(raw) % 16 != 0:
           raw += bytes(16 - (len(raw) % 16))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(password, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
