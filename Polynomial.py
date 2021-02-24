import random

'''
Clase para trabajar con los polinomios
'''


class Polynomial:
    '''
    Constructor de la clase
    :param n: La cantidad mínima de evaluaciones para desencriptar
    '''

    def __init__(self, n):
        self.n = n

    '''
    Genera un polinomio de grado self.n-1
    :param k: El término independiente del polinomio
    :return: Una lista con los coeficientes del polinomio
    '''

    def generate(self, k):
        polynomial = [None] * self.n
        for i in range(self.n):
            polynomial[i] = random.randint(1, 1000)
        polynomial[self.n - 1] = k
        return polynomial

    '''
    Implementación del algoritmo de Horner para evaluar polinomios
    :param x: El valor donde evaluaremos el polinomio
    :param polynomial: El polinomio que evaluaremos
    :return: El resultado de la evaluación
    '''

    def horner(self, x, polynomial):
        result = polynomial[0]
        for i in range(1, self.n):
            result = (result * x) + polynomial[i]
        return result
