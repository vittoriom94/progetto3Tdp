import xlrd
from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from TdP_collections.map.binary_search_tree import TreeMap
from campionato import Campionato
from giornata import Giornata


class DatiPartite:
  __slots__= 'campionati', 'associazioni_squadre'
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
    dati_riga[1] = int(dati_riga[1])
    dati_riga[2] = xlrd.xldate_as_tuple(dati_riga[2],0)
    dati_riga[5] = int(dati_riga[5])
    dati_riga[6] = int(dati_riga[6])
    dati_riga[8] = int(dati_riga[8])
    dati_riga[9] = int(dati_riga[9])

    if dati_riga[0] in self.campionati:
      c = self.campionati[dati_riga[0]]
    else:
      c = Campionato(dati_riga[0])
      self.campionati[dati_riga[0]] = c

    c.inserisci_partita(dati_riga, new_sheet)
    self.associazioni_squadre[dati_riga[3]] = dati_riga[0]

  def get_campionato(self, campionato):
    return self.campionati[campionato]

  def get_campionato_from_squadra(self, squadra):
    return self.associazioni_squadre[squadra]

  def print_dati(self):
    for campionato in self.campionati.values():
      for giornata in campionato.giornate.values():
        for partita in giornata.partite.values():
          print(campionato.nome + " " + str(giornata.n_giornata) + ": " + str(giornata.data_inizio) + " - " + str(giornata.data_fine) + " -> " + str(partita))