from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from partita import Partita


class Giornata:
  __slots__ = 'n_giornata','partite','data_inizio','data_fine'

  def __init__(self, n_giornata):
    self.n_giornata = n_giornata
    self.partite = ProbeHashMap()
    self.data_inizio = (2016, 1, 1, 0, 0, 0)
    self.data_fine = (2017, 12, 31, 0, 0, 0)

  def inserisci_partita(self, partita):

    p = Partita(partita[3],partita[4],partita[5],partita[6],partita[7],partita[8],partita[2],partita[1])
    self.partite[partita[3]] = p
    self.partite[partita[4]] = p
    return p
