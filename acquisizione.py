import xlrd
from dati import DatiPartite

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


if __name__ == "__main__":
  path = "partite.xlsx"
  a = Acquisizione()
  a.acquisisci(path)
