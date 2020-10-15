from RPA.Excel.Files import Files

def read_excel_worksheet(path, worksheet):
    lib = Files()
    lib.open_workbook(path)
    try:
        return lib.read_worksheet(worksheet)
    finally:
        lib.close_workbook()

if __name__ == '__main__':
    data1 = read_excel_worksheet('sample.xlsx', 'Sheet1')
    for d in data1:    
        print(d['A'], d['B'])
    data2 = read_excel_worksheet('sample.xlsx', 'Sheet2')
    for d in data2:    
        print(d['A'], d['B'], d['C'])