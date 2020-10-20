class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        import math
        
        if self.a < (self.b + self.c) and self.b < (self.a + self.c) and self.c < (self.a + self.b):
            lados = [self.a, self.b, self.c]
            cateto_b = float(min(lados))
            lados.remove(cateto_b)
            cateto_c = float(min(lados))
            lados.remove(cateto_c)
            hipotenusa = float(min(lados))
            
            if int(hipotenusa)**2 == int(cateto_b)**2 + int(cateto_c)**2:
                return True
            else:
                return False
        else:
            return print('não é possivel formar triangulo com essas medidas')
       
