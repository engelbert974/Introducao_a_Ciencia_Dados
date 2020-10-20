def éprimo(k):
    fator = 2
    if k == 2:
        return print(k)
    while k % fator != 0 and fator <= k / 2:
        fator = fator + 1  
    if k % fator == 0:
        return 0  
    else:
        return 1

def maior_primo(n):
    i = 1
    while n > 0:
        if éprimo(n) == 1:
            return n
        else:
            n = n - i
            
        
    


