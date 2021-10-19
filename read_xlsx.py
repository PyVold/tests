import xlrd
# pip install xlrd==1.2.0

sheet = xlrd.open_workbook('test.xlsx')

wb = sheet.sheets()
names = sheet.sheet_names()


for i in names:
    print(i)

for x in wb:
    print(x)
    for y in range(x.nrows):
        print(x.row_values(y))
    for z in range(x.ncols):
        print(x.col_values(y))
