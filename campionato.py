from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from TdP_collections.map.binary_search_tree import TreeMap
from giornata import Giornata


class Campionato:
  __slots__= 'nome','giornate','counter','data_partite'
  def __init__(self,nome):
    self.giornate = TreeMap()
    self.data_partite = ProbeHashMap()
    self.nome = nome
    self.counter = 0

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

    if dati_riga[1] in self.giornate:
      g = self.giornate[dati_riga[1]]
    else:
      g = Giornata(dati_riga[1])
      self.giornate[dati_riga[1]] = g
    p = g.inserisci_partita(dati_riga)
    self.aggiungi_partita_in_lista(p, dati_riga[2])
    self.controllo_giornata(g, dati_riga[1],dati_riga[2], new_sheet)

  def aggiungi_partita_in_lista(self, partita, data):
    if data in self.data_partite:
      lista_partite = self.data_partite[data]
      lista_partite.append(partita)
    else:
      lista_partite = list()
      lista_partite.append(partita)
      self.data_partite[data] = lista_partite

  def get_giornata(self, n_giornata):
    return self.giornate[n_giornata]

  def controllo_giornata(self,g, n, data, new_sheet):
    if new_sheet:
      self.counter = n
      g.data_inizio = data
      g.data_fine = (2017, 12, 31, 0, 0, 0)
      #setta nuova giornata iniziata
    elif (n-self.counter) == 1:
      #setta fine giornata di counter e nuova giornata di n
      g.data_inizio = data
      self.giornate[self.counter].data_fine = data
      self.counter = n

    elif n == self.counter:
      pass