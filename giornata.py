from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from partita import Partita


class Giornata:
  __slots__ = 'n_giornata','partite','data_inizio','data_fine'

  def __init__(self, n_giornata):
    self.n_giornata = n_giornata
    self.partite = ProbeHashMap()

  def inserisci_partita(self, partita):
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
    p = Partita(partita[3],partita[4],partita[5],partita[6],partita[8],partita[9],partita[2],partita[1])
    self.partite[partita[3]] = p
    self.partite[partita[4]] = p
    return p

  def get_partita(self, squadra):
    return self.partite[squadra]