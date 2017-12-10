import xlrd
from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from TdP_collections.map.binary_search_tree import TreeMap
from campionato import Campionato
from giornata import Giornata


class DatiPartite:
  __slots__= 'campionati'
  def __init__(self):
    self.campionati = ProbeHashMap()


  def inserisci_partita(self, dati_riga, new_sheet=False):

    if dati_riga[0] in self.campionati:
      c = self.campionati[dati_riga[0]]
    else:
      c = Campionato(dati_riga[0])
      self.campionati[dati_riga[0]] = c

    c.inserisci_partita(dati_riga, new_sheet)

  def get_campionato_from_squadra(self, squadra):
    for c in self.campionati:
      if squadra in self.campionati[c].giornate[1].partite:
        return self.campionati[c]
    raise KeyError

  def print_dati(self):
    file = open("log.txt", "w+")
    file.truncate()
    for campionato in self.campionati.values():
      for i in range(1, len(campionato.giornate)+1):
        giornata = campionato.giornate[i]
        for partita in giornata.partite.values():
          print(campionato.nome + " " + str(giornata.n_giornata) + ": " + str(giornata.data_inizio) + " - " + str(giornata.data_fine) + " -> " + str(partita))
          file.write(campionato.nome + " " + str(giornata.n_giornata) + ": " + str(giornata.data_inizio) + " - " + str(giornata.data_fine) + " -> " + str(partita) + "\n")
    file.close()