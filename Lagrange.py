def inverse(a):
    return pow(a, -1, Lagrange.MOD)


def _sum(a, b):
    return (a + b) % Lagrange.MOD


def _prod(a, b):
    return (a * b) % Lagrange.MOD


'''
Clase para evaluar el polinomio de Lagrange
'''


class Lagrange:
    MOD = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    '''
    Evalúa el polinomio de Lagrange en 0 y regresa el resultado
    :param x: Una lista con valores en el eje x
    :param y: Una lista con valores en el eje y
    :return : El resultado de evaluar el polinomio de Lagrange en 0 
    '''

    @staticmethod
    def password(x, y):
        value = 0
        for i in range(len(x)):
            p = 1
            for j in range(len(x)):
                if i != j:
                    x[i] %= Lagrange.MOD
                    x[j] %= Lagrange.MOD
                    inv = inverse(x[i] - x[j])
                    p = _prod(p, _prod(-x[j], inv))
            value = _sum(value, _prod(p, y[i]))
        return int(value)
