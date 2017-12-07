import xlrd
from dati import DatiPartite
from requests import Richieste


class Acquisizione:
    def acquisisci(self, nome):
        dim=11
        dati=DatiPartite()
        book = xlrd.open_workbook(nome)
        for sheet in book.sheets():
            cell=dim*[None]
            for i in range(1, sheet.nrows):
                for j in range(0, sheet.ncols):
                    cell[j]=sheet.cell(i,j).value
                new = True if i==1 else False
                dati.inserisci_partita(cell, new)
        dati.print_dati()
        return dati


if __name__ == "__main__":
  path = "partite.xlsx"
  a = Acquisizione()
  dati = a.acquisisci(path)

  r = Richieste(dati)

  print("Esercizio uno")
  c = input("inserisci campionato: ")
  l = r.richiesta_uno(str(c))
  print(list(l))
  #
  # print("Esercizio due")
  # g = input("inserisci giornata: ")
  # c = input("inserisci campionato: ")
  # classifica,avversari = r.richiesta_due(int(g), str(c))
  # print(str(classifica))
  # print(list(avversari))
  # print(list(avversari.values()))
  #
  # print("Esercizio tre")
  # g = input("inserisci giornata: ")
  # c = input("inserisci campionato: ")
  # classifica,avversari = r.richiesta_tre(int(g), str(c))
  # print(str(classifica))
  # print(list(avversari))
  # print(list(avversari.values()))


  # print("Esercizio quattro")
  # g = input("inserisci giornata: ")
  # s = input("inserisci squadra: ")
  # risultato= r.richiesta_quattro(int(g), str(s))
  # print(str(risultato))
  #
  # print("Esercizio cinque")
  # d = input("inserisci data in formato AAAA,M,G (2016,9,2): ")
  # risultato = r.richiesta_cinque(d)
  # print(risultato)
  #
  #
  #
  # print("Esercizio sei")
  # g = input("inserisci giornata: ")
  # n = input("inserisci n: ")
  # risultato = r.richiesta_sei(int(g), int(n))
  # print(risultato)
  #
  # print("Esercizio sette")
  # g = input("inserisci giornata: ")
  # n = input("inserisci n: ")
  # risultato = r.richiesta_sei(int(g), int(n))
  # print(risultato)


  # print("Esercizio otto")
  # g = input("inserisci giornata: ")
  # n = input("inserisci n: ")
  # risultato = r.richiesta_sei(int(g), int(n))
  # print(risultato)

  # print("Esercizio nove")
  # g = input("inserisci giornata: ")
  # c = input("inserisci campionato: ")
  # risultato = r.richiesta_nove(int(g), str(c))
  # print(risultato)