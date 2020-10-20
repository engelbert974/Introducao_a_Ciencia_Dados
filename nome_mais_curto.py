def mais_curto(lista_de_nomes):
    i = 0
    while i < len(lista_de_nomes) - 1:
        j = i + 1
        while j < len(lista_de_nomes):
            x = len(lista_de_nomes[i].strip())
            y = len(lista_de_nomes[j].strip())
            if x < y:
                j = j + 1
            else:
                i = i + 1
    return lista_de_nomes[i].strip().capitalize()
        
