import os
from io import StringIO
import xlwt

result_data = [["a1", "b1", "c1", "d1"], ["e1", "f1", "g1", "h1"], ["i1", "j1", "k1", "l1"]]
sheets = ["Sheet 1"]

wb = xlwt.Workbook()
file_name = "output.xls"
for sheet, data in zip(sheets, [result_data]):
    ws = wb.add_sheet(sheet)
    for row, row_value in enumerate(data):
        for col, col_value in enumerate(row_value):
            ws.write(row, col, col_value)

wb.save(file_name)
