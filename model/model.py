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
        lista_minori = []
        lista_maggiori = []
        for arco in self.G.edges.data('peso'):
            peso = arco[2]
            if peso < S:
                lista_minori.append(arco)
            if peso > S:
                lista_maggiori.append(arco)
        return len(lista_minori), len(lista_maggiori)
