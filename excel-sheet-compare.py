import xlrd

def WorkbooktoDictbysheetname(file_name, sheet_name):
    sheet_data = []
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_name(sheet_name)
    for row in range(sheet.nrows):
        row_data = []
        for cell in sheet.row_values(row):
            try:
                row_data.append(str(cell.encode('utf8')))
            except:
                row_data.append(cell)
        sheet_data.append(row_data)
    return sheet_data


source_file = "1.xlsm"
ref_file = "2.xlsm"

ref_data = WorkbooktoDictbysheetname(ref_file,'Other')
source_data = WorkbooktoDictbysheetname(source_file,'Other')


for index, source_row in enumerate(source_data):
    ref_row = ref_data[index]
    for pos ,item in enumerate(source_row):
        if item != ref_row[pos]:
            print "*"*25+"Item Miss match"+"*"*25
            print "source file row No :%s position:%s: Item:%s"%(index, pos,item)
            print "Ref File row No:%s position:%s: Item:%s"%(index, pos,ref_row[pos])
            print "*"*60
