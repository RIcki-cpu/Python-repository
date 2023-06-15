class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):

    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2

class Circulo():
    def __init__(self,radio): #radio en metros
        self.radio=radio
    def area(self):
        return 3.1416*pow(self.radio,2)


rectangulo = Rectangulo(20, 10)
triangulo = Triangulo(20, 12)
circulo = Circulo(12)

print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())
print("Área del circulo:", circulo.area())
