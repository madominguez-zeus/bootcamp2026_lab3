class Calculadora:
    def __init__(self, servicio_externo = None):
        self.servicio_externo = servicio_externo
        self.resultado = 0

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b
    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b


