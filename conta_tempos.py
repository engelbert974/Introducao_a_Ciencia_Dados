import Ordenador
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] # clona a lista1 com os mesmos valores

        o = Ordenador.Ordenador()

        print("Comparando com listas aleatórias")
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        print("\nComparando com listas quase ordenadas")

        lista3 = self.lista_quase_ordenada(n)
        lista4 = lista3[:]
        
        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista4)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)
    
