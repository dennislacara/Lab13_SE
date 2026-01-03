import flet as ft
import networkx as nx

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # Dati importati dal Model
        #creazione e implementazione del grafo
        self._model.costruzione_grafo()
        #estrazione dati
        n_nodi = self._model.G.number_of_nodes()
        n_archi = self._model.G.number_of_edges()
        minimo, massimo = self._model.min_max_peso()

        #Dati importati nella View
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Numero di vertici {n_nodi} - Numero di archi {n_archi}'))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Informazioni sui pesi degli archi - Minimo: {minimo} & Massimo: {massimo}'))
        self._view.update()
        print('lista_visualizzazione_1 aggiornata nella UI')

        # TODO

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        #controllo che il grafo sia stato generato
        if not self._model.G:
            self._view.show_alert('Grafo inesistente')
            return
        input_Conta_archi = self._view.txt_name.value

        if input_Conta_archi and input_Conta_archi.isdigit() and int(input_Conta_archi) in [3,4,5,6,7]:
            Nminori, Nmaggiori = self._model.conta_archi(int(input_Conta_archi))
            #Dati importati nella View
            self._view.lista_visualizzazione_2.controls.clear()
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f'Numero di archi con peso minore della soglia {Nminori}'))
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f'Numero di archi con peso maggiore della soglia {Nmaggiori}'))
            self._view.update()
            print('lista_visualizzazione_2 aggiornata nella UI')

        else:
            self._view.show_alert(f'Soglia non valida;\nIl valore è di tipo: {"Numerico" if input_Conta_archi.isdigit() else "Non numerico"};\nSoglia compresa tra 3 e 7!!!')
        # TODO

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        if not self._model.archi_soglia:
            self._view.show_alert('Impostare una soglia')
            return

        #eseguo la ricerca del percorso piu pesante ed estraggo i dati utili
        percorso, peso = self._model.best_arco_()
        print(percorso, peso)
        lunghezza = len(percorso) - 1

        self._view.lista_visualizzazione_3.controls.clear()
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f'Numero di archi percorso più lungo: {lunghezza}'))
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f'Peso cammino massimo: {peso}'))
        for i in range(len(percorso)-1):
            partenza = percorso[i]
            arrivo = percorso[i+1]
            grafo = self._model.G
            peso_arco = grafo[partenza][arrivo]['peso']

            self._view.lista_visualizzazione_3.controls.append(ft.Text(f'{partenza} --> {arrivo} : {peso_arco}'))
        self._view.update()

        # TODO