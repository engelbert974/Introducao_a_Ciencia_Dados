import math
const_a = float(input("Digite o valor da constante 'a': "))
const_b = float(input("Digite o valor da constante 'b': "))
const_c = float(input("Digite o valor da constante 'c': "))

delta = (const_b**2 - 4*const_a*const_c)

if delta > 0:
    x1 = (- const_b + math.sqrt(delta)) / (2*const_a)
    x2 = (- const_b - math.sqrt(delta)) / (2*const_a)
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
else:
    if delta == 0:
        x3 = (- const_b) / (2*const_a)
        print("a raiz desta equação é", x3)
    else:
        if delta < 0:
            print("esta equação não possui raízes reais")
    
    
    
