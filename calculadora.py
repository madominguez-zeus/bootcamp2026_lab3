def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", suma(num1, num2))
    print("Resta:", resta(num1, num2))
    print("Multiplicación:", multiplicacion(num1, num2))

if __name__ == "__main__":
    calculadora()
