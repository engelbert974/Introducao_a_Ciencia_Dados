def soma_matrizes(m1, m2):

    lin1 = len(m1)
    col1 = len(m1[0])

    lin2 = len(m2)
    col2 = len(m2[0])

    if lin1 == lin2 and col1 == col2:
        soma_matrizes = []
        for i in range(lin1):
            linha = []
            for j in range(col1):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)

            soma_matrizes.append(linha)
        return soma_matrizes
    
    else:
        return False
    
