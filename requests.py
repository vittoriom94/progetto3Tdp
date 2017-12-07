from Heapify import Heapify
from TdP_collections.hash_table.probe_hash_map import ProbeHashMap


class Richieste:
  def __init__(self, dati):
    self.dati = dati


  def richiesta_tre(self,g, c):
    if g <1:
      raise Exception("Giornata inferiore a 1")
    campionato = self.dati.campionati[c]
    classifica_no = ProbeHashMap()
    avversari = ProbeHashMap()
    try:
      data_finale = campionato.giornate[g].data_fine
    except KeyError:
      data_finale = (2017,12,31,0,0,0)
    for i in range(1,g+1):
      if i not in campionato.giornate:
        break
      giornata = campionato.giornate[i]
      for squadra in giornata.partite:
        partita = giornata.partite[squadra]
        #aggiorna classifica
        if partita.data <= data_finale:    #se la partita è rinviata a dopo la giornata indicata allora non viene contata
          if squadra not in classifica_no:
            classifica_no[squadra] = 0
          classifica_no[squadra] = classifica_no[squadra] + self._checkrisultato_pt_n(squadra, partita)
          #aggiorna avversari
          if squadra not in avversari:
            avversari[squadra] = 0
          avversari[squadra]+=1
      print(list(classifica_no))
    classifica_o = sorted(classifica_no, key=lambda item : classifica_no[item],reverse=True) #sorted = O(nlogn)
    return classifica_o,avversari

  def _checkrisultato_pt_n(self,squadra, partita):
    if squadra == partita.casa:
      if partita.risultato_primo_tempo() == "H":
        return 3
      elif partita.risultato_primo_tempo() == "A":
        return 0
    if squadra == partita.ospite:
      if partita.risultato_primo_tempo() == "H":
        return 0
      elif partita.risultato_primo_tempo() == "A":
        return 3
    return 1

  def richiesta_quattro(self, giornata, squadra):
    if giornata <1:
      raise Exception("Giornata inferiore a 1")
    risultati = list()
    start = giornata-4 if giornata >= 5 else 1
    campionato = self.dati.campionati[self.dati.associazioni_squadre[squadra]]
    for i in range(start, giornata+1):
      if i not in campionato.giornate:
        break
      #controllare eccezione quando giornata è troppo grande
      partita = campionato.giornate[i].partite[squadra]
      risultato = self._checkrisultato_str(squadra, partita)
      print("Risultato: " + risultato + " partita: " + str(partita))
      risultati.append(risultato)
    return risultati

  def _checkrisultato_str(self,squadra, partita):
    if squadra == partita.casa:
      if partita.risultato_finale() == "H":
        return "Win"
      elif partita.risultato_finale() == "A":
        return "Defeat"
    if squadra == partita.ospite:
      if partita.risultato_finale() == "H":
        return "Defeat"
      elif partita.risultato_finale() == "A":
        return "Win"
    return "Tie"




  def richiesta_cinque(self, data):
    data = str(data).split(",")
    data = (int(data[0]), int(data[1]), int(data[2]), 0, 0, 0)
    print(data)
    risultati = list()
    for campionato in self.dati.campionati.values():
      for n_giornata in campionato.giornate:
        giornata = campionato.giornate[n_giornata]
        for squadra in giornata.partite:
          partita = giornata.partite[squadra]
          if partita.data == data:
            risultato = campionato.nome +": "+partita.casa + " - " + partita.ospite + ": " + partita.risultato_finale()
            risultati.append(risultato)
    return risultati

  ### stampare anche il numero di gol?
  def richiesta_sei(self,g, n):
    if g <1:
      raise Exception("Giornata inferiore a 1")
    classifica_no = ProbeHashMap()
    for campionato in self.dati.campionati.values():
      for i in range(1, g + 1):
        if i not in campionato.giornate:
          break
        giornata = campionato.giornate[i]
        for squadra in giornata.partite:
          partita = giornata.partite[squadra]
          if squadra not in classifica_no:
            classifica_no[squadra] = 0
          classifica_no[squadra]-= partita.gol_casa if squadra == partita.casa else partita.gol_ospite

    #classifica_o = sorted(classifica_no, key=lambda item: classifica_no[item], reverse=True)  # sorted = O(nlogn)
    h = Heapify(classifica_no)
    classifica_o = list()
    for i in range(1, n):
      classifica_o.append(h.remove_min()._value)
    return classifica_o[0:n]

  def richiesta_sette(self, g, n):
    if g < 1:
      raise Exception("Giornata inferiore a 1")
    classifica_no = ProbeHashMap()
    for campionato in self.dati.campionati.values():
      for i in range(1, g + 1):
        if i not in campionato.giornate:
          break
        giornata = campionato.giornate[i]
        for squadra in giornata.partite:
          partita = giornata.partite[squadra]
          if squadra not in classifica_no:
            classifica_no[squadra] = 0
          classifica_no[squadra] += partita.gol_ospite if squadra == partita.casa else partita.gol_casa

    #classifica_o = sorted(classifica_no, key=lambda item: classifica_no[item])  # sorted = O(nlogn)

    h = Heapify(classifica_no) #O n
    classifica_o = list()
    for i in range(1, n): #O klogn  k sarebbe n
      classifica_o.append(h.remove_min()._value)
    return classifica_o[0:n]

  def richiesta_otto(self, g, n):
    if g < 1:
      raise Exception("Giornata inferiore a 1")
    classifica_no = ProbeHashMap()
    for campionato in self.dati.campionati.values():
      for i in range(1, g + 1):
        if i not in campionato.giornate:
          break
        giornata = campionato.giornate[i]
        for squadra in giornata.partite:
          partita = giornata.partite[squadra]
          if squadra not in classifica_no:
            classifica_no[squadra] = 0
          diff = partita.gol_casa - partita.gol_ospite
          classifica_no[squadra] -= diff if squadra == partita.casa else -diff

    #classifica_o = sorted(classifica_no, key=lambda item: classifica_no[item], reverse=True)  # sorted = O(nlogn)

    h = Heapify(classifica_no)
    classifica_o = list()
    for i in range(1, n):
      classifica_o.append(h.remove_min()._value)
    return classifica_o[0:n]

  ### Gestire parimerito?
  def richiesta_nove(self,g, c):
    if g <1:
      raise Exception("Giornata inferiore a 1")
    campionato = self.dati.campionati[c]
    classifica_no = ProbeHashMap()
    try:
      data_finale = campionato.giornate[g].data_fine
    except KeyError:
      data_finale = (2017,12,31,0,0,0)
    for i in range(1,g+1):
      if i not in campionato.giornate:
        break
      giornata = campionato.giornate[i]
      for squadra in giornata.partite:
        partita = giornata.partite[squadra]
        #aggiorna classifica
        if partita.data <= data_finale:    #se la partita è rinviata a dopo la giornata indicata allora non viene contata
          if squadra not in classifica_no:
            classifica_no[squadra] = [0,0,0] # [WIN, WIN in casa, WIN in trasferta]
          r1 = 1 if self._checkrisultato_str(squadra,partita) == "Win" else 0
          r2 = 1 if squadra == partita.casa and partita.risultato_finale() == "H" else 0
          r3 = 1 if squadra == partita.ospite and partita.risultato_finale() == "A" else 0
          print(partita, r1, r2, r3, squadra)
          old_r = classifica_no[squadra]
          classifica_no[squadra] = [old_r[0] + r1, old_r[1] + r2, old_r[2] + r3]
    return self._check_top(classifica_no)


  def _check_top(self, classifica):
    top = None
    risultati = None
    print(list(classifica))
    print(list(classifica.values()))
    for squadra in classifica:
      print(top)
      new_r = classifica[squadra]
      if top is None:
        top = [squadra, squadra, squadra]
        risultati = new_r
      else:
        for i in range(0,3):
          if risultati[i] < new_r[i]:
            risultati[i] = new_r[i]
            top[i] = squadra
    return top