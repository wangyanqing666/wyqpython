
import xlrd

data = xlrd.open_workbook('C:\\Users\\asus\\PycharmProjects\\untitled\\TestDate\\demo.xlsx')
tables =data.sheet_names()
print(tables)
sheet1=data.sheet_by_name('Sheet1')

print(sheet1.row_values(1)[0])
print(sheet1.row(0))
print(sheet1.cell(0,1).value)