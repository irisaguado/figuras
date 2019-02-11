
class Figura():
    def __init__(self):
        return None

    def calcular_perimetro(self):
        return None

    def calcular_area(self):
        return None

class Triangulo(Figura):
    def __init__(self, altura, base, lado1, lado2):
        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        area = (self.altura * self.base)/2
        return area

    def calcular_perimetro(self):
        perimetro = self.base + self.lado1 + self.lado2
        return perimetro

triangulo1 = Triangulo(5,2,3,6)
print(triangulo1.calcular_area())
print(triangulo1.calcular_perimetro())
