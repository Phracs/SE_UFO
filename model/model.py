from networkx.classes import neighbors

from UI import view
from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.lista_sightings=[]
        self._grafo=nx.Graph()
        self._view=view
        self.lista_stati=[]




    def crea_grafo(self, anno:int, shape:str):
        self._grafo = nx.Graph()
        self.crea_nodi()

        count=DAO.conta_avvistamenti_per_stato(anno, shape)

        neighbors=DAO.read_neighbors()

        for a, b in neighbors:
            peso= count.get(a,0) + count.get(b,0)
            if peso>0:
                self._grafo.add_edge(a, b, weight=peso)



    def crea_nodi(self):
        self.lista_stati=DAO.read_stati()
        for s in self.lista_stati:
            self._grafo.add_node(s.id.strip().upper())

    def crea_archi(self):
        for a, b in DAO.read_neighbors():
            self._grafo.add_edge(a, b)

    def somme_pesi_adiacenti(self):
        res = [(n, self._grafo.degree(n, weight="weight")) for n in self._grafo.nodes]
        res.sort(key=lambda x: x[1], reverse=True)
        return res

