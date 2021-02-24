import Secret
import Clear
import sys
import getpass

'''
Solicita la información pertinente al usuario para encriptar y 
procede a encriptar
'''


def encriptar():
    fragments = input("Nombre de archivo donde se guardarán las evaluaciones (sin extensión): ")
    try:
        n = int(input("Número de evaluaciones: "))
        t = int(input("Número de evaluaciones minimas: "))
    except ValueError:
        sys.exit("Asegúrate de ingresar un valor númerico.")
    clear = input("Nombre de archivo a encriptar: ")
    password = getpass.unix_getpass("Contraseña: ")
    secret = Secret.Secret(password)
    secret.encrypt(clear)
    secret.fragments(t, n, fragments)


'''
Solicita la información pertinente al usuario para desencriptar y 
procede a desencriptar
'''


def desencriptar():
    points = input("Nombre de archivo con las t evaluaciones: ")
    dark = input("Archivo cifrado: ")
    decrypt = Clear.Clear(dark)
    message = decrypt.decrypt(points)
    decrypt.write_decrypted(message)


'''
Main del programa
'''


def main():
    print("Escribe el nombre de los archivos con extensión, a menos de que se"
          + " indique lo contrario.")
    while True:
        action = input("Encriptar (c) | Desencriptar (d) | Salir (Cualquier otro caracter): ")
        if action == 'c':
            encriptar()
        elif action == 'd':
            desencriptar()
        else:
            break


if __name__ == "__main__":
    main()
