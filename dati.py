from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from TdP_collections.map.binary_search_tree import TreeMap
from campionato import Campionato
from giornata import Giornata


class DatiPartite:
  __slots__= 'campionati, associazioni_squadre'
  def __init__(self):
    self.campionati = TreeMap()
    self.associazioni_squadre = ProbeHashMap()
  def inserisci_partita(self, dati_riga, new_sheet=False):
    # 0 - campionato
    # 1 - giornata
    # 2 - data
    # 3 - home
    # 4 - ospite
    # 5 - fthg
    # 6 - ftag
    # 7 - ftr
    # 8 - hthg
    # 9 - htag
    # 10 - htr

    if dati_riga[0] in self.campionati:
      c = self.campionati[dati_riga[0]]
    else:
      c = Campionato(dati_riga[0])

    c.inserisci_partita(dati_riga, new_sheet)
    self.associazioni_squadre[dati_riga[3]] = dati_riga[0]

  def get_campionato(self, campionato):
    return self.campionati[campionato]

