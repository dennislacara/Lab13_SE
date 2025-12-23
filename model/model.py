import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()

        self.geni = None
        self.map_geni = None

        self.interazioni = None


        self.load_geni()
        #self.load_interazioni()


    def load_geni(self):
        self.geni, self.map_geni = DAO.get_all_geni()

    def load_interazioni(self):
        self.interazioni = DAO.get_all_interazioni()
