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
    
    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
