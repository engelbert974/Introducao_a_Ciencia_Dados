def menor_nome(nomes):
    i = 0
    nomeRe = nomes[i].strip()
    while i < int(len(nomes) - 1):
        j = i + 1
        #nome = print ("o", i + 1, "nome é", nomes[i])
        while j < int(len(nomes)):
            #nome = print ("nome conjugado é", nomes[i] + " " + nomes[j])
            if len(nomes[i].strip()) <= len(nomes[j].strip()):
                if len(nomes[i].strip()) < len(nomeRe):
                    nomeRe = nomes[i].strip()
                    j += 1
                else:
                    j += 1
            else:
                #nomeRe = '' nomes[j].strip()
                j += 1
        i += 1
    return nomeRe.capitalize()
