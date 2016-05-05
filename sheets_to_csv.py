import xlrd
import csv

workbook = xlrd.open_workbook('excel.xls')
sheet_names =  workbook.sheet_names()


for index, each_sheet in enumerate(sheet_names):
	print each_sheet
	csv_data = []
	xl_sheet = workbook.sheet_by_index(index)
	num_cols = xl_sheet.ncols
	for row_idx in range(0, xl_sheet.nrows):
		each_row = []
		for col_idx in range(0, num_cols):
			cell_obj = xl_sheet.cell(row_idx, col_idx)
			each_cell =  str(cell_obj).split(':')[1]
			each_row.append(str(each_cell))
			print str(each_cell.encode("utf-8"))
		csv_data.append(each_row)
		
		with open('%s.csv'%each_sheet, 'wb') as fp:
			a = csv.writer(fp, delimiter=',',quotechar='|', quoting=csv.QUOTE_NONE)
			a.writerows(csv_data)
