def maiusculas(frase):
    tam = 0
    ASCII = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    string = ""
    while tam < len(frase):
        if ord(frase[tam]) in ASCII:
            string = string + frase[tam]
            tam += 1
        else:
            tam += 1
    return string
