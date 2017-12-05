import xlrd

# ----------------------------------------------------------------------
def open_file(path):
  """
  Open and read an Excel file
  """
  book = xlrd.open_workbook(path)

  # print number of sheets
  print(book.nsheets)

  # print sheet names
  print(book.sheet_names())

  # get the first worksheet
  first_sheet = book.sheet_by_index(0)

  # read a row
  print(first_sheet.row_values(0))

  # read a cell
  cell = first_sheet.cell(0, 0)
  print(cell)
  print(cell.value)

  # read a row slice

  for i in range(1,first_sheet.nrows):

    x = first_sheet.cell(i,1).value
    if isinstance(x,float):
      x = int(x)
    print(x,end=" - ")
    #print("aaa- " + str(first_sheet.row_values(i)))
    print(xlrd.xldate_as_tuple(first_sheet.cell(i,2).value, 0), end=" - ")
    print(first_sheet.cell(i,3).value,end=" - ")
    print(first_sheet.cell(i,4).value,end=" - ")
    print(first_sheet.cell(i,5).value,end=" - ")
    print(first_sheet.cell(i,6).value,end=" - ")
    print(first_sheet.cell(i,7).value,end=" - ")
    print(first_sheet.cell(i,8).value)

  stringa1 = "riga1cella1,riga1cella2,riga1cella3;riga2cella1,riga2cella2,riga2cella3;riga3cella1,riga3cella2,riga3cella3"
  righe = stringa1.split(";");
  for r in righe:
    colonne = r.split(",")
    for c in colonne:
      print(c, end=" - ")
    print("\n")

  print(first_sheet.row_slice(rowx=0,
                        start_colx=0,
                        end_colx=2))


# ----------------------------------------------------------------------
if __name__ == "__main__":
  path = "partite.xlsx"
  open_file(path)

#
# for row...:
#   riga = 11*[None]
#   for colonna...:
#     riga[colonna] = sheet.cell(row,colonna).value
#   dati.insert_riga(riga)