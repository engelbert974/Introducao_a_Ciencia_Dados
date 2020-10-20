l = int(input("digite a largura: "))
h = int(input("digite a altura: "))
cont_lin = 1
cont_col = 1

while cont_col <= h:
    while cont_lin <= l:
        if cont_col == 1:
            print("#", end = '')
            cont_lin = cont_lin + 1
        elif cont_col > 1 and cont_col < l:
            print("#", " "  end = '')
            cont_lin = cont_lin + 1
    cont_col = cont_col + 1
    print()
    cont_lin = 1
