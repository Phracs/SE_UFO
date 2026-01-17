import flet as ft

from database.dao import DAO


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.lista_anni = []

    def populate_dd(self,dd_year):
        """ Metodo per popolare i dropdown """
        #TODO
        lista_anni= DAO.read_anni()
        for a in lista_anni:
            dd_year.options.append(ft.dropdown.Option(str(a)))

    def populate_dd2(self,dd_shape):
        """ Metodo per popolare i dropdown """
        #TODO
        year= int(self._view.dd_year.value)
        lista_shapes= DAO.read_shapes(year)
        for a in lista_shapes:
            dd_shape.options.append(ft.dropdown.Option(str(a)))

    def handle_year_change(self, e:ft.ControlEvent):
        year_str=e.control.value
        dd=self._view.dd_shape
        year=int(year_str)
        forme=DAO.read_shapes(year)
        dd.options.clear()
        dd.options.extend([ft.dropdown.Option(f) for f in forme])
        self._view.dd_shape.disabled= False
        self._view.update()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        # TODO
        year= int(self._view.dd_year.value)
        shape= self._view.dd_shape.value
        self._model.crea_grafo(year, shape)

        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato (anno={year}, forma={shape} - "
                f"nodi={self._model._grafo.number_of_nodes()}, archi={self._model._grafo.number_of_edges()})"))
        for stato, somma in self._model.somme_pesi_adiacenti():
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Nodo{stato}: somma pesi su archi:{somma}"))
        self._view.update()




    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
