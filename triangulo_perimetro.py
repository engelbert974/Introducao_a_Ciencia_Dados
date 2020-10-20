def main():
    t = Triangulo(1, 1, 1)

    t.lado_a()
    t.lado_b()
    t.lado_c()
    t.perimetro()

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perim = 0

    def lado_a(self):
        return self.a

    def lado_b(self):
        return self.b

    def lado_c(self):
        return self.c

    def perimetro(self):
        self.perim = 0
        self.perim = self.a + self.b + self.c
        return self.perim

main()
       
