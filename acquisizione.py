import datetime

import xlrd
from TdP_collections.map.binary_search_tree import TreeMap
from dati import DatiPartite
from requests import Richieste


class Acquisizione:
  def acquisisci(self, nome):
    """ Acquisizione da file originale """
    sheets = ["E0","SC0","D1","SP1","I1","F1","N1","B1","P1","T1","G1"]
    dim = 10
    self.dati = DatiPartite()
    book = xlrd.open_workbook(nome)
    for sheet in book.sheets():
      # itera solo sui fogli richiesti in traccia
      if sheet.name not in sheets:
        continue
      # costruisci la lista di squadre a partire dalla colonna delle squadre, set per eliminare i duplicati
      self.elenco_squadre = list(set(sheet.col_values(2,1,sheet.nrows)))
      # inizializza lista di squadre non inserite per la prima giornata
      self.not_inserite = list(self.elenco_squadre)
      self.elenco_rinvii = TreeMap() # collection delle squadre rinviate
      cell = dim * [None]
      self.counter = 1 # giornata 1
      self.next = None # riga successiva
      self.prev = None # riga precedente
      for i in range(1, sheet.nrows):
        for j in range(0, dim):
          cell[j] = sheet.cell(i, j).value # vettore con dati della riga i
        if i < sheet.nrows-1: # compila next a meno
          next = dim*[None]
          for j in range(0, dim):
            next[j] = sheet.cell(i+1, j).value
          self.next = self._formatta_riga_originale(next)
        new_sheet = True if i == 1 else False # true se è la prima riga di un foglio
        if not new_sheet: # inizializza prev, la prima riga non ne ha una precedente
          prev = dim * [None]
          for j in range(0, dim):
            prev[j] = sheet.cell(i-1, j).value
          self.prev = self._formatta_riga_originale(prev)
        cell = self._formatta_riga_originale(cell)

        rinvio = self._check_giornata(cell) # controlla la riga
        if rinvio == 0: # la riga appartiene alla giornata corrente
          self._remove_from_not_inserite(cell)
          cell[1] = self.counter
        else: # la riga è un rinvio
          cell[1] = rinvio
        self.dati.inserisci_partita(cell, new_sheet) # inserisci la riga nella struttura
    return self.dati

  def _check_other_match(self, riga, missingValue):
    """ Controlla se la partita successiva avviene a distanza di due giorni """
    data = datetime.datetime(*riga[2])
    if self.next is None: # riga è l'ultima partita del campionato
      return True
    data2 = datetime.datetime(*self.next[2])
    diff = data2-data
    if diff.days > 1:
      return True
    else:
      if self.next[3] in missingValue and self.next[4] in missingValue: # controlla se la partita successiva è presente in missingValue
        return True
      return False

  def _check_rinvio(self, riga):
    """ ritorna la giornata a cui inserire la partita se è un rinvio, 0 altrimenti"""
    s1, s2 = riga[3], riga[4] #squadra casa, squadra ospite
    if self.elenco_rinvii.is_empty(): # non ci sono partite rinviate finora
      return 0
    for pos in self.elenco_rinvii.inorder(): # controlla dal meno recente al più recente
      missingKey, missingValue = pos.key(), pos.value()
      if s1 in missingValue and s2 in missingValue: # lista di squadre che non hanno giocato per quella giornata, se s1 e s2 sono nella lista allora può essere un rinvio
        if len(missingValue) > 2: #con due o più partite rinviate, possono esserci più combinazioni
          # controlla se la giornata successiva avviene a meno di due giorni di distanza,
          # in questo caso anche la successiva deve essere un rinvio, altrimenti si assume che la partita corrente sia una nuova giornata
          if not self._check_other_match(riga, missingValue):
            return 0
        missingValue.remove(s1)
        missingValue.remove(s2)
        self.elenco_rinvii.delete(pos)
        # aggiorna collection dei rinvii
        if len(missingValue) != 0:
          self.elenco_rinvii[missingKey] =  missingValue
        return missingKey
    return 0

  def _is_over_two(self, riga):
    """ Controlla se la partite corrente avviene a più di due giorni di distanza dalla precedente"""
    data = datetime.datetime(*riga[2])
    if self.prev is None:
      return False
    data2 = datetime.datetime(*self.prev[2])
    diff = data - data2
    if diff.days > 2:
      return True
    return False

  def _check_giornata(self, riga):
    """ Calcola a quale giornata appartiere una partita, ritorna 0 se la partita appartiene a self.counter, altrimenti
    ritorna la giornata a cui appartiene (in caso di rinvio) """
    s1,s2 = riga[3], riga[4] # squadra casa, squadra ospite
    new = self._is_over_two(riga) # se true, allora la partita è un rinvio o una nuova giornata
    #una delle due ha già giocato, controlla prima per un rinvio e poi inserisci
    if (s1 not in self.not_inserite or s2 not in self.not_inserite) or new:
      i = self._check_rinvio(riga) # controlla se la partita può essere un rinvio, se i!=0 allora è un rinvio, altrimenti per i=0 è una nuova giornata
      if i == 0:
        # crea una lista di squadre che non hanno giocato per questa giornata, in modo da salvare i rinvii
        lista = list()
        for squadra in self.not_inserite:
          lista.append(squadra)
        if len(lista) != 0:
          self.elenco_rinvii[self.counter] = lista #salva la lista nella collection dei rinvii
        self.counter +=1 # incrementa giornata corrente
        self.not_inserite = list(self.elenco_squadre) # resetta lista di squadre non inserite
        return 0
      else:
        return i # la partita è un rinvio, ritorna la giornata a cui inserirla
    return 0 # nessuna delle due ha già giocato per la giornata corrente

  def _remove_from_not_inserite(self,riga):
    s1, s2 = riga[3], riga[4]
    self.not_inserite.remove(s1)
    self.not_inserite.remove(s2)

  def acquisisci_mod(self, nome):
    dim = 10
    self.dati = DatiPartite()
    book = xlrd.open_workbook(nome)
    for sheet in book.sheets():
      cell = dim * [None]
      for i in range(1, sheet.nrows):
        self.counter = 1
        for j in range(0, 10):
          cell[j] = sheet.cell(i, j).value
        new = True if i == 1 else False
        cell = self._formatta_riga_modificato(cell)
        self.dati.inserisci_partita(cell, new)
    return self.dati

  def _formatta_riga_originale(self, dati_riga):
    """ Formatta la riga nel formato accettato dalla struttura """
    riga = [None]*10
    riga[0] = dati_riga[0] #campionato
    riga[2] = xlrd.xldate_as_tuple(dati_riga[1],0) #data
    riga[3] = dati_riga[2] #squadra 1
    riga[4] = dati_riga[3] #squadra 2
    riga[5] = int(dati_riga[4]) if dati_riga[4] is not '' else 0 # gol squadra casa
    riga[6] = int(dati_riga[5]) if dati_riga[5] is not '' else 0 # gol squadra ospite
    riga[8] = int(dati_riga[7]) if dati_riga[7] is not '' else 0 # gol squadra casa primo tempo
    riga[9] = int(dati_riga[8]) if dati_riga[8] is not '' else 0 # gol squadra ospite primo tempo
    return riga

  def _formatta_riga_modificato(self, dati_riga):
    dati_riga[1] = int(dati_riga[1])
    dati_riga[2] = xlrd.xldate_as_tuple(dati_riga[2],0)
    dati_riga[5] = int(dati_riga[5])
    dati_riga[6] = int(dati_riga[6])
    dati_riga[8] = int(dati_riga[8])
    dati_riga[9] = int(dati_riga[9])
    return dati_riga

if __name__ == "__main__":
  # path = "partite.xlsx"
  # a = Acquisizione()
  # dati = a.acquisisci_mod(path)

  path = "originale.xls"
  a = Acquisizione()
  dati = a.acquisisci(path)
  r = Richieste(dati)

  print("Esercizio uno")
  c = input("inserisci campionato: ")
  l = r.richiesta_uno(str(c))
  print(list(l))

  print("Esercizio due")
  g = input("inserisci giornata: ")
  c = input("inserisci campionato: ")
  classifica,avversari = r.richiesta_due(int(g), str(c))
  string = "Squadra - Punti - Partite giocate:\n"
  for element in classifica:
    pg = avversari[element[0]]
    string+=element[0]+" - "+str(element[1])+" - "+str(pg)+"\n"
  print(string)


  print("Esercizio tre")
  g = input("inserisci giornata: ")
  c = input("inserisci campionato: ")
  classifica,avversari = r.richiesta_tre(int(g), str(c))
  print(str(classifica))
  print(list(avversari))
  print(list(avversari.values()))


  print("Esercizio quattro")
  g = input("inserisci giornata: ")
  s = input("inserisci squadra: ")
  risultato= r.richiesta_quattro(int(g), str(s))
  print(str(risultato))

  print("Esercizio cinque")
  d = input("inserisci data in formato AAAA,M,G (2016,9,2): ")
  risultato = r.richiesta_cinque(d)
  print(risultato)



  print("Esercizio sei")
  g = input("inserisci giornata: ")
  n = input("inserisci n: ")
  risultato = r.richiesta_sei(int(g), int(n))
  print(risultato)

  print("Esercizio sette")
  g = input("inserisci giornata: ")
  n = input("inserisci n: ")
  risultato = r.richiesta_sei(int(g), int(n))
  print(risultato)


  print("Esercizio otto")
  g = input("inserisci giornata: ")
  n = input("inserisci n: ")
  risultato = r.richiesta_sei(int(g), int(n))
  print(risultato)

  print("Esercizio nove")
  g = input("inserisci giornata: ")
  c = input("inserisci campionato: ")
  risultato = r.richiesta_nove(int(g), str(c))
  print(risultato)
