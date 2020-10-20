def computador_escolhe_jogada(n, m):

    if n == m:

        return n

    else:
        
        quantia = n % (m + 1)

        if quantia > 0:

            return quantia

        return m



def usuario_escolhe_jogada(n, m):
    
    jogada = 0

    while jogada == 0:
        
        jogada = int(input("Quantas peças você vai tirar? "))
        #print(" ")

        if jogada > n or jogada < 1 or jogada > m:
            print(" ")
            print("Oops! Jogada inválida! Tente de novo.")
            print(" ")
            jogada = 0

    return jogada
    

def partida():

    n = 0
    m = 0

    while n == 0 or m == 0:
    
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        if n <=0 or m <= 0 or n < m:
            n = 0
            m = 0

    estrategia = True

    if n % (m + 1) == 0:
        estrategia = False
        print(" ")
        print("Você começa")
        print(" ")
    
    else:
        print(" ")
        print("Computador começa")
        print(" ")
    
    while n > 0:

        if estrategia:
            
            #print(" ")
            jogada = computador_escolhe_jogada(n, m)
            estrategia = False

            if jogada == 1 and n == 1:
                print("O computador tirou uma peça.")
            
            elif jogada == 1 and n > 1:
                print("O computador tirou uma peça.")
            
            elif jogada > 1 and n == 1:
                print("O computador tirou", jogada, "peças.")

            elif jogada > 1 and n > 1:
                print("O computador tirou", jogada, "peças.") 
        else:
            #print(" ")
            jogada = usuario_escolhe_jogada(n, m)
            estrategia = True

            if jogada == 1 and n == 1:
                print("Você tirou uma peça.")
            
            if jogada == 1 and n > 1:
                print("Você tirou uma peça.")
            
            if jogada > 1 and n == 1:
                print("Você tirou", jogada, "peças.")

            if jogada > 1 and n > 1:
                print("Você tirou", jogada, "peças.")

        n = n - jogada
        if jogada == 1 and n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print(" ")
            
        if jogada == 1 and n > 1:
            print("Agora restam apenas", n, "peças no tabuleiro.")
            print(" ")
            
        if jogada > 1 and n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print(" ")

        if jogada > 1 and n > 1:
            print("Agora restam apenas", n, "peças no tabuleiro.")
            print(" ")

    if estrategia:
        print("Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

    

def campeonato():

    usuario = 0
    computador = 0
    
    rodada = 1
    while rodada <= 3:
        print(" ")
        print("**** Rodada", rodada, "****")
        print(" ")
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1

            if (rodada == 3):
                print(" ")
                print("**** Final do campeonato! ****")
                print(" ")
                print("Placar final: Você  {} x {}  Computador".format(usuario, computador))

        rodada = rodada + 1


def main():

    jogo = 0

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - para jogar uma partida isolada")
    jogo = int(input("2 - para jogar um campeonato "))
    print(" ")

    if jogo == 1:
        print("Você escolheu uma partida isolada!")
        print(" ")
        partida()
    elif jogo == 2:
        print("Você escolheu um campeonato!")
        #print(" ")
        campeonato()
    else:
        print("Opção inválida!")
        jogo = 0


main()
