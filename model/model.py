
import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = None

        self.cromosomi = None
        self.map_geni = None

        self.interazioni = None


        self.load_geni()
        self.load_interazioni()

    def costruzione_grafo(self):
        #creazione grafo
        self.G = nx.DiGraph()
        #implementazione nodi
        self.G.add_nodes_from(self.cromosomi)
        #implementazione archi
        for tupla in self.interazioni:
            self.G.add_edge(tupla[0], tupla[1], peso=tupla[2])
        print('Grafo implementato')

    def load_geni(self):
        self.cromosomi, self.map_geni = DAO.get_all_geni()

    def load_interazioni(self):
        self.interazioni = DAO.get_all_interazioni()

    def min_max_peso(self):
        min = float('inf')
        max = float('-inf')
        for arco in self.G.edges.data('peso'):
            valore = arco[2]
            if valore < min:
                min = valore
            if valore > max:
                max = valore
        return min, max

    def conta_archi(self, S):
        self.archi_soglia = None
        lista_minori = []
        lista_maggiori = []
        for arco in self.G.edges.data('peso'):
            peso = arco[2]
            if peso < S:
                lista_minori.append(arco)
            if peso > S:
                lista_maggiori.append(arco)
                #incremento di una lista del Model che contiene gli archi superiori alla soglia
                if not self.archi_soglia:
                    self.archi_soglia = [arco]
                else:
                    self.archi_soglia.append(arco)
        return len(lista_minori), len(lista_maggiori)

    def best_arco_(self):
        #creo un grafo relativo con gli archi validi
        grafo = nx.DiGraph()
        for arco in self.archi_soglia:
            grafo.add_edge(arco[0], arco[1], peso=arco[2])

        self.best_arco = []
        self.peso_ottimo = float('-inf')
        self.ricorsione(grafo, grafo.nodes, [])

        return self.best_arco, self.peso_ottimo

    def ricorsione(self,grafo, nodi, l_parziale):
        if len(l_parziale)>=2:
            peso = nx.path_weight(grafo, l_parziale, 'peso')
            if peso > self.peso_ottimo:
                self.best_arco = l_parziale.copy()
                self.peso_ottimo = peso
                print(self.best_arco)
                print(self.peso_ottimo)

        for nodo in nodi:

            #caso in cui c'è un incrocio e si ripete un nodo
            if nodo in l_parziale:
                l_parziale.append(nodo)
                v = list(nx.neighbors(grafo, nodo))
                vicini = [vicino for vicino in v if vicino not in l_parziale]

            #caso semplice
            else:
                l_parziale.append(nodo)
                vicini = list(nx.neighbors(grafo, nodo))

            #ricorsione
            self.ricorsione(grafo, vicini, l_parziale)
            #backtracking
            l_parziale.pop(-1)
