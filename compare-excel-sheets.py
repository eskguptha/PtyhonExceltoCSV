import xlrd

def WorkbooktoDictbysheetname(file_name):
    workbook_data = {}
    workbook = xlrd.open_workbook(file_name)
    for sheet_name in workbook.sheet_names():
        sheet_data = []
        sheet = workbook.sheet_by_name(sheet_name)
        for row in range(sheet.nrows):
            row_data = []
            for cell in sheet.row_values(row):
                try:
                    row_data.append(str(cell.encode('utf8')))
                except:
                    row_data.append(cell)
            sheet_data.append(row_data)
        workbook_data[sheet_name] = sheet_data
    return workbook_data


source_file = "1.xlsm"
ref_file = "2.xlsm"

ref_data = WorkbooktoDictbysheetname(ref_file)
source_data = WorkbooktoDictbysheetname(source_file)

for key, sheet_rows in source_data.items():
    ref_file = ref_data[key]
    for index, source_row in enumerate(sheet_rows):
        ref_row = ref_file[index]
        for pos ,item in enumerate(source_row):
            if item != ref_row[pos]:
                print "*"*25+"Item Miss match in %s Sheet"%key.title()+"*"*25
                print "source file row No :%s position:%s: Item:%s"%(index, pos,item)
                print "Ref File row No:%s position:%s: Item:%s"%(index, pos,ref_row[pos])
                print "*"*60 
