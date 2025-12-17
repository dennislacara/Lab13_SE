import networkx as nx

from database import dao
from database.dao import DAO

class Model:

    def __init__(self):
        self.G = nx.DiGraph()
        self.cromosomi = None #list
        self.load_cromosomi()
        print(self.cromosomi)
        self.geni = None #dict
        self.load_geni()
        self.interazioni = None
        self.create_graph()

    def create_graph(self):
        #implementazione dei nodi del grafo
        self.G.add_nodes_from(self.cromosomi)
        #importazione delle interazioni e implementazione del grafo
        self.interazioni = dao.DAO.read_all_interazioni()
        for interazione in self.interazioni:
            id_gene1 = interazione.id_gene1
            id_gene2 = interazione.id_gene2
            print(self.geni[id_gene2])
            if nx.is_path(self.G, (self.geni[id_gene1], self.geni[id_gene2])):
                self.G[self.geni[id_gene1]][self.geni[id_gene2]]['peso'] += interazione.correlazione
            else:
                self.G.add_edge(self.geni[id_gene1], self.geni[id_gene2], peso=interazione.correlazione)
        return print(self.G)



    def load_cromosomi(self):
        self.cromosomi = DAO.read_all_cromosomi()
    def load_geni(self):
        self.geni = DAO.read_all_geni()