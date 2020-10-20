def retangulo(largura, altura, caractere):
    print(caractere * largura) # cabeçalho

    for i in range(altura - 2):
        espacos = (largura - 2) * ' '
        print("%s%s%s" % (caractere, espacos, caractere)) # meio

    print(caractere * largura) # rodapé

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
caractere = "#"

retangulo(largura, altura, caractere)
