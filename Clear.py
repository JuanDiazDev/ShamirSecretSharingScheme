import base64
import Lagrange
import sys
from Crypto.Cipher import AES

'''
Clase que se ocupa del proceso de desencriptación
'''


class Clear:
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    '''
    Constructor de la clase
    :param dark: El archivo a desencriptar
    '''

    def __init__(self, dark):
        self.dark = dark

    '''
    Obtiene la llave a partir de las evaluaciones dadas y la usa para 
    desencriptar el archivo oscuro.
    :param points: El archivo con las evaluaciones para desencriptar
    :except IOError, IndexError, Value Error
    :return: El mensaje desencriptado. Regresa una cadena vacía si la desencriptación falla
    '''

    def decrypt(self, points):
        x, y = [], []
        try:
            with open(points) as file:
                for line in file:
                    point = line.split()
                    x.append(int(point[0]))
                    y.append(int(point[1]))
        except (IOError, IndexError, ValueError):
            sys.exit("Asegúrate de que el archivo con los fragmentos"
                     + " exista y contenga dos enteros separados por un espacio"
                     + " en cada renglón.")
        lag = Lagrange.Lagrange()
        key = lag.password(x, y)
        return self.decrypt_secret(key)

    '''
    Escribe un archivo con el mensaje desencriptado
    :param secret: El mensaje desencriptado
    :except IOError
    '''

    def write_decrypted(self, secret):
        try:
            clear = open(self.dark[:-4] + ".clear", "w+")
            clear.write(secret)
            clear.close()
        except IOError:
            sys.exit("Ha ocurrido un error escribiendo el archivo desencriptado")

    '''
    Método auxiliar para desencriptar el archivo a partir de la llave dada
    :param key: La llave generada por la evaluación del polinomio de Lagrange
    :except IOError
    :return: El mensaje desencriptado
    '''

    def decrypt_secret(self, key: int):
        enc = ""
        password = key.to_bytes(32, "big")
        try:
            with open(self.dark) as d:
                for line in d:
                    enc += line
        except IOError:
            sys.exit("Ha ocurrido un error leyendo el archivo con el mensaje encriptado")
        lens = len(enc)
        enc = enc[2:lens - 1].encode('utf_8')
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(password, AES.MODE_CBC, iv)
        return Clear.unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
