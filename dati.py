from TdP_collections.map.binary_search_tree import TreeMap


class DatiPartite:

  def __init__(self):
    self.giornate = TreeMap()

  def inserisci_partita(self, dati_riga):
    # 0 - campionato
    # 1 - giornata
    # 2 - data
    # 3 - home
    # 4 - opsite
    # 5 - fthg
    # 6 - ftag
    # 7 - ftr
    # 8 - hthg
    # 9 - htag
    # 10 - htr
    g = self.giornate[dati_riga[1]]
    pass

  def get_giornata(self, n_giornata):
    return self.giornate[n_giornata]