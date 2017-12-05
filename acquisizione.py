import xlrd
from dati import DatiPartite

class Acquisizione:
    def acquisisci(self, nome):
        dim=100
        dati=DatiPartite()
        book = xlrd.open_workbook(nome)
        for sheet in book.sheets():
            cell=dim*[None]
            for i in range(1, sheet.nrows()):
                for j in range(0, sheet.ncols()):
                    cell[j]=sheet.cell(i,j)
                dati.inserisci_partita(cell)
