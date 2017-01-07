import csv

source_file = "1.tsv"
ref_file = "2.tsv"

def CSVtoDict(file_name,delimiter):
    csv_data = []
    for row in csv.DictReader(open(file_name),delimiter=delimiter):
        csv_data.append(row)
    return csv_data

source_data = CSVtoDict(source_file, '\t')
ref_data = CSVtoDict(ref_file,',')

for index, source_row in enumerate(source_data):
    ref_row = ref_data[index]
    for key ,value in source_row.items():
        if key in ref_row:
            if source_row[key] != ref_row[key]:
                print "*"*25+ key+" value Miss match"+"*"*25
                print "source file row No :%s Key:%s: Value:%s"%(index, key,value)
                print "Ref File row No:%s Key:%s: Value:%s"%(index, key,ref_row[key])
                print "*"*60
        else:
            print "*"*25+"Key is Missing ("+ key +") in Ref File"+"*"*25
            print "source file row No :%s Key:%s: Value:%s"%(index,key,value)
            print "Ref File row No:%s Key:%s: Value:"%(index, key)
            print "*"*60
