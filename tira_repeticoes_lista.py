def remove_repetidos(lista):
    i=0
    while i < len(lista) - 1:
        j=i+1
        while j < len(lista):
            if lista[i]==lista[j]:
                del lista[j]
            else:
                j=j+1
        i=i+1
    sorted(lista)
    return lista
        
